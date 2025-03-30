# Customs ETL Automation

A practical ETL solution for automating the processing of customs XML declarations and integrating them with shipping data for fast and accurate report generation.

## 🚀 Problem

Originally, the workflow relied on manually unpacking XML files, copying data into Google Sheets, and using formulas. This approach was slow, unstable for large datasets (~450+ rows), and inefficient — often requiring hours of manual work and a dedicated employee.

## ✅ Solution

This project automates the entire process by:
- Parsing XML customs declaration files and storing relevant data into an SQLite database.
- Matching that data against shipping info from CSV files.
- Generating an Excel report with matched records, all in under 5 minutes.

## 📈 Impact

This automation reduced the report preparation time from **4–6 hours per report** (manual labor in Google Sheets) to **under 5 minutes**, eliminating the need for a dedicated full-time employee.

Assuming one full-time employee previously spent 68 hours/month on this task 
⏱️ Time before automation: 68 hours/month
⚡ Time with this utility: ~2 hours/month
💸 Net savings: 66 hours/month of manual work eliminated
💡 I'm proud to have transformed a slow, manual, and fragile process into an elegant Python-based solution.  
This project demonstrates both technical skills and real-world business impact.

## 🧠 Skills & Technologies

- Python 🐍
- SQLite
- ETL Automation
- XML Parsing
- Data Matching (fuzzy string comparison)
- Excel Report Generation
- Tkinter UI for file selection

## 📂 Project Structure

- `separatedDB1.py` — Extracts goods info from customs XML files and inserts it into an SQLite database.
- `CSVcheckDB.py` — Compares shipping CSV data to the customs data, enriches it with MRN and item numbers, and generates a final Excel report.

## 🔧 How to Use

1. Run `separatedDB1.py`  
   → Select one or more XML files (customs declarations).

2. Run `CSVcheckDB.py`  
   → Select the CSV file with shipping data.

3. The script will compare and enrich your data.  
   → Output will be saved as `*MRNdone.xlsx` in the same directory.

## 🔐 Data Privacy

All sensitive data (names, IDs, etc.) has been removed or anonymized. The scripts are safe for demo or test usage.

## 🧰 Future Improvements

- Web-based UI
- Support for SQLCipher encryption
- Logging & error handling


