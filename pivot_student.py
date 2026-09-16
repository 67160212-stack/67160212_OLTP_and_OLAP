from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parent

with sqlite3.connect((ROOT / 'data' / 'warehouse.db').as_uri() + '?mode=ro', uri=True) as con:
    df = pd.read_sql_query('SELECT * FROM sales', con)

print("=== Source Data ===")
print(df.head())

# P1: province x month
p1 = pd.pivot_table(df, index='province', columns='month', values='amount', aggfunc='sum', fill_value=0, margins=True, margins_name='Total')
print("\n=== P1: Pivot Province x Month ===")
print(p1)

# P2: Filter September, then category x province
df_sep = df[df['month'] == '2026-09']
p2 = pd.pivot_table(df_sep, index='category', columns='province', values='amount', aggfunc='sum', fill_value=0, margins=True, margins_name='Total')
print("\n=== P2: September Category x Province ===")
print(p2)

# P3: Assert Grand Total
grand_total_pivot = p1.loc['Total', 'Total']
grand_total_df = df['amount'].sum()
assert grand_total_pivot == grand_total_df, f"Mismatch: {grand_total_pivot} != {grand_total_df}"
print("\n=== P3: Assert Passed! Grand Total =", grand_total_pivot)

# P4: Export to CSV
p1.to_csv(ROOT / 'pivot_province_month.csv')
p2.to_csv(ROOT / 'pivot_september.csv')
print("Exported CSV files successfully.")