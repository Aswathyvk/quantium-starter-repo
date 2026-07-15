import pandas as pd
import glob

# Read and combine all three CSV files
files = glob.glob("data/daily_sales_data_*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Keep only Pink Morsel rows
df = df[df["product"].str.strip().str.lower() == "pink morsel"]

# Clean price (remove $ sign) and compute sales
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
df["sales"] = df["price"] * df["quantity"]

# Keep required columns, rename to match spec
output = df[["sales", "date", "region"]].rename(
    columns={"sales": "Sales", "date": "Date", "region": "Region"}
)

output.to_csv("data/output.csv", index=False)
print("Done. Rows:", len(output))