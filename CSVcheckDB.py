
import sqlite3
import pandas as pd
from fuzzywuzzy import fuzz
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
csv_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV Files", "*.csv")])
if not csv_path:
    print("No file selected. Exiting.")
    exit()

DB_PATH = "separated.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

csv_df = pd.read_csv(csv_path, encoding="utf-8", low_memory=False)
csv_df.columns = [str(i+1) for i in range(len(csv_df.columns))]

csv_df["MRN"] = None
csv_df["declarationGoodsItemNumber"] = None

cursor.execute("SELECT TransportDocument, SupportingDocument_1, descriptionOfGoods, MRN, declarationGoodsItemNumber FROM Goods")
db_rows = cursor.fetchall()

for index, row in csv_df.iterrows():
    transport_doc = str(row["1"]).strip()
    supporting_doc = str(row["4"]).strip()
    desc_goods = str(row["8"]).strip()

    for db_row in db_rows:
        db_transport_doc, db_supporting_doc, db_desc_goods, db_mrn, db_decl_goods_item = db_row

        if transport_doc == db_transport_doc and supporting_doc == db_supporting_doc:
            similarity = fuzz.ratio(desc_goods.lower(), str(db_desc_goods).lower())
            if similarity >= 85:
                csv_df.at[index, "MRN"] = db_mrn
                csv_df.at[index, "declarationGoodsItemNumber"] = db_decl_goods_item
                break

conn.close()

output_path = csv_path.replace(".csv", "MRNdone.xlsx")
csv_df.to_excel(output_path, index=False)
print(f"File saved: {output_path}")
