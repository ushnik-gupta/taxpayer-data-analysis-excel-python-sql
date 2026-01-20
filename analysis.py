import pandas as pd

# Load dataset
df = pd.read_csv("tax_business_data.csv")

print("Dataset Preview:")
print(df.head())

print("\nTotal Records:", len(df))

# Average income by city
avg_income_city = df.groupby("City")["Annual_Income"].mean()
print("\nAverage Income by City:")
print(avg_income_city)

# Tax regime distribution
tax_regime_count = df["Tax_Regime"].value_counts()
print("\nTax Regime Distribution:")
print(tax_regime_count)

# Compliance status count
compliance_count = df["Compliance_Status"].value_counts()
print("\nCompliance Status Distribution:")
print(compliance_count)

# Average tax payable (correct column used)
avg_tax = df["Tax_Payable"].mean()
print("\nAverage Tax Payable:", avg_tax)

# Example of high tax payers
high_tax = df[df["Tax_Payable"] > df["Tax_Payable"].mean()]
print("\nHigh Tax Payers Above Average:")
print(high_tax[["Taxpayer_ID", "Annual_Income", "Tax_Payable"]])
import sqlite3

conn = sqlite3.connect("tax_analysis.db")

query = """
SELECT City, AVG(Tax_Payable) AS Avg_Tax
FROM taxpayers
GROUP BY City
ORDER BY Avg_Tax DESC;
"""

sql_result = pd.read_sql(query, conn)
print("\nAverage Tax Payable by City (SQL):")
print(sql_result)

conn.close()


