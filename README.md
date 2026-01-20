# 📊Project 3: Taxpayer Data Analysis (Excel + Python + SQL)

## 🔍 Project Overview
This project demonstrates an end-to-end data analytics workflow using **Excel, Python, and SQL**.  
The objective is to analyze taxpayer financial data to derive income insights, tax regime trends, and compliance behavior—similar to real-world analytics work done in consulting and audit firms like **PwC**.

The project covers:
- Data preparation and validation in Excel
- Data analysis using Python (Pandas)
- Relational database creation using SQLite
- Analytical querying using SQL

---

## 🛠️ Tools & Technologies Used
- **Microsoft Excel** – Data creation and cleaning
- **Python 3.13** – Data analysis
- **Pandas** – Data manipulation
- **SQLite** – Lightweight relational database
- **SQL** – Analytical querying
- **VS Code** – Development environment

---

## 📁 Project Structure
```text
pwc_project_3/
├── tax_business_data.csv     # Cleaned dataset (from Excel)
├── analysis.py               # Python data analysis script
├── create_db.py              # SQLite database creation script
├── tax_analysis.db           # SQLite database (auto-generated)
├── queries.sql               # SQL analytical queries
└── README.md                 # Project documentation
```
## 📊 Dataset Description
The dataset represents individual taxpayers with the following attributes:

Taxpayer_ID

Age

City

Profession

Annual_Income

Tax_Regime (Old / New)

Total_Deductions

Taxable_Income

Tax_Payable

Compliance_Status (Filed / Late / Not Filed)

## 🧮 Python Analysis (analysis.py)
The Python script performs:

Dataset loading and validation

Total record count analysis

Average income by city

Tax regime distribution

Compliance status distribution

Identification of high tax payers

Summary statistics for business decision-making

Sample insights generated:

Cities with the highest average income

Distribution between Old vs New tax regimes

Tax compliance behavior patterns

High-value taxpayers contributing maximum tax revenue

## 🗄️ Database Creation (create_db.py)
Converts the cleaned CSV dataset into a SQLite database

Creates a structured table named taxpayers

Enables SQL-based analytics similar to production systems

Database file generated:

tax_analysis.db

## 🧾 SQL Analysis (queries.sql)
The SQL file contains business-focused analytical queries, including:

Full taxpayer record inspection

Average income by city

Tax regime distribution analysis

High-income taxpayer identification

Compliance status summary

Top tax contributors

These queries simulate real consulting-style data exploration.

## 🎯 Key Skills Demonstrated
Data cleaning and validation

Exploratory Data Analysis (EDA)

SQL querying and aggregation

Financial & tax data interpretation

End-to-end analytics pipeline

Professional project documentation

## 📌 Why This Project Matters
This project reflects real-world analytics work performed in:

Tax & compliance analytics

Financial reporting

Consulting & advisory teams

It is specifically designed to align with PwC Intern – Technology / Data Analytics roles.

## 🚀 How to Run the Project
1️⃣ Run Python Analysis
```bash

python analysis.py
```
2️⃣ Create SQLite Database
```bash

python create_db.py
```
3️⃣ Execute SQL Queries
Open queries.sql in any SQLite client or DB Browser and run queries on tax_analysis.db.

## 👤 Author
Ushnik Gupta
B.Tech (CSE) | BS Data Science & Applications (IIT Madras)
Aspiring Data & Technology Consultant


