import pandas as pd
import os

# ============================================================
# Ireland Housing Affordability Analysis - Data Cleaning Script
# Client: Focus Ireland | Dataset: CSO HPA02
# Association: UCC MSc Business Analytics
# ============================================================

# 1. Load raw data
df = pd.read_csv("HPA02.csv")

print("Raw dataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# 2. Initial profiling
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# 3. Drop missing values in VALUE column
df_clean = df.dropna(subset=["VALUE"]).copy()
print(f"\nRows after dropping missing VALUE: {len(df_clean)} (removed {len(df) - len(df_clean)} rows)")

# 4. Standardise column names to snake_case
df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)
print("\nStandardised columns:", df_clean.columns.tolist())

# 5. Fix data types
df_clean["year"] = df_clean["year"].astype(int)
df_clean["value"] = pd.to_numeric(df_clean["value"], errors="coerce")

# 6. Standardise categorical values
for col in ["county", "dwelling_status", "type_of_buyer", "type_of_sale", "statistic_label"]:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].str.strip().str.title()

# 7. Filter to market sales only
df_market = df_clean[df_clean["type_of_sale"] == "Market"].copy()

# 8. Filter out aggregate rows
df_county = df_market[df_market["county"] != "National"].copy()

# 9. Summary table - County x Year
median_price = df_county[
    (df_county["statistic_label"].str.contains("Median", case=False, na=False)) &
    (df_county["type_of_buyer"].str.contains("All", case=False, na=False)) &
    (df_county["dwelling_status"].str.contains("All", case=False, na=False))
][["county", "year", "value"]].rename(columns={"value": "median_price"})

volume = df_county[
    (df_county["statistic_label"].str.contains("Volume", case=False, na=False)) &
    (df_county["type_of_buyer"].str.contains("All", case=False, na=False)) &
    (df_county["dwelling_status"].str.contains("All", case=False, na=False))
][["county", "year", "value"]].rename(columns={"value": "volume"})

mean_price = df_county[
    (df_county["statistic_label"].str.contains("Mean", case=False, na=False)) &
    (df_county["type_of_buyer"].str.contains("All", case=False, na=False)) &
    (df_county["dwelling_status"].str.contains("All", case=False, na=False))
][["county", "year", "value"]].rename(columns={"value": "mean_price"})

county_summary = (
    median_price
    .merge(volume, on=["county", "year"], how="outer")
    .merge(mean_price, on=["county", "year"], how="outer")
)

# 10. Summary table - Dwelling Status by Year
dwelling_summary = df_county[
    (df_county["statistic_label"].str.contains("Median|Volume", case=False, na=False)) &
    (df_county["type_of_buyer"].str.contains("All", case=False, na=False)) &
    (df_county["dwelling_status"].str.contains("New|Existing", case=False, na=False))
].copy()

# 11. Summary table - Buyer Type
buyer_summary = df_county[
    (df_county["statistic_label"].str.contains("Volume", case=False, na=False)) &
    (df_county["dwelling_status"].str.contains("All", case=False, na=False)) &
    (~df_county["type_of_buyer"].str.contains("All", case=False, na=False))
].groupby(["year", "type_of_buyer"])["value"].sum().reset_index()
buyer_summary.rename(columns={"value": "volume"}, inplace=True)

# 12. Key statistics
print("\nKey Statistics (2024)")
print("="*40)
stats_2024 = county_summary[county_summary["year"] == 2024]
if not stats_2024.empty:
    print(f"Avg median price (2024): EUR {stats_2024['median_price'].mean():,.0f}")
    max_row = stats_2024.loc[stats_2024['median_price'].idxmax()]
    min_row = stats_2024.loc[stats_2024['median_price'].idxmin()]
    print(f"Highest: {max_row['county']} - EUR {max_row['median_price']:,.0f}")
    print(f"Lowest:  {min_row['county']} - EUR {min_row['median_price']:,.0f}")
    print(f"Price gap: EUR {max_row['median_price'] - min_row['median_price']:,.0f}")

# 13. Export clean CSV files
os.makedirs("cleaned_data", exist_ok=True)
county_summary.to_csv("cleaned_data/county_summary.csv", index=False)
dwelling_summary.to_csv("cleaned_data/dwelling_summary.csv", index=False)
buyer_summary.to_csv("cleaned_data/buyer_summary.csv", index=False)
df_clean.to_csv("cleaned_data/HPA02_cleaned.csv", index=False)

print("\nExported 4 clean CSV files to /cleaned_data/")
print("Done: county_summary.csv")
print("Done: dwelling_summary.csv")
print("Done: buyer_summary.csv")
print("Done: HPA02_cleaned.csv")