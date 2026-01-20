import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("tax_business_data.csv")

# Create SQLite DB
conn = sqlite3.connect("tax_analysis.db")

# Write to SQL table
df.to_sql("taxpayers", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully with table: taxpayers")
