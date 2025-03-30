
import sqlite3
import xml.etree.ElementTree as ET
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Goods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descriptionOfGoods TEXT,
            declarationGoodsItemNumber TEXT,
            MRN TEXT,
            TransportDocument TEXT,
            SupportingDocument_1 TEXT,
            SupportingDocument_2 TEXT
        )
    ''')
    conn.commit()
    conn.close()

def parse_and_insert(xml_files, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for goods_item in root.findall('.//GoodsItem'):
            description = goods_item.findtext('.//descriptionOfGoods', '')
            descriptions = description.split(';') if ';' in description else [description]

            item_number = goods_item.findtext('.//declarationGoodsItemNumber', '')
            mrn = root.findtext('.//MRN', '')
            transport_doc = goods_item.findtext('.//TransportDocument/referenceNumber', '')
            supporting_docs = [doc.findtext('referenceNumber', '') for doc in goods_item.findall('.//SupportingDocument')]

            while len(supporting_docs) < 2:
                supporting_docs.append('')

            for desc in descriptions:
                cursor.execute('''
                    INSERT INTO Goods (descriptionOfGoods, declarationGoodsItemNumber, MRN, TransportDocument, SupportingDocument_1, SupportingDocument_2)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (desc.strip(), item_number, mrn, transport_doc, supporting_docs[0], supporting_docs[1]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_name = "separated.db"
    Tk().withdraw()
    xml_files = askopenfilenames(title="Select XML files", filetypes=[("XML files", "*.xml")])

    if xml_files:
        create_database(db_name)
        parse_and_insert(xml_files, db_name)
        print("Data successfully added to database.")
    else:
        print("No files selected.")
