import pandas as pd

file_path = "C:/...the path to your file.../"

items_df = pd.read_csv(file_path + "items.csv")

# multiple AND conditons
print(items_df[(items_df["gross_weight"] >= 15) & (items_df["units"] >= 10)])

# multiple OR conditions
print(items_df[(items_df["gross_weight"] >= 15) | (items_df["units"] >= 10)])

# SQL-like BETWEEN/AND
print(items_df[(items_df["gross_weight"] >= 15) | (items_df["gross_weight"] <= 16)])

# SQL-like IN (...)
print(items_df[items_df["item_code"].isin(["84500", "84400"])])

# SQL-like wildcard match %text%
print(items_df[items_df["item_description"].str.contains("SHORT")])

# SQL-like wildcard match %text
print(items_df[items_df["item_description"].str.startswith("COOKIE")])

# SQL-like wildcard match text%
print(items_df[items_df["item_description"].str.endswith("BAR")])

# complex filter using masks
mask_min_weight = (items_df["gross_weight"] >= 15)
mask_max_weight = (items_df["gross_weight"] <= 16)
mask_min_units = (items_df["units"] > 10)
mask_max_units = (items_df["units"] < 25)
print(items_df[((mask_min_weight & mask_max_weight) | (mask_min_units & mask_max_units))])