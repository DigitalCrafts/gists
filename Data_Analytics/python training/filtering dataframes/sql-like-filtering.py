import pandas as pd

items_df = pd.read_csv("items.csv")

print("multiple AND conditons")
print(items_df[(items_df["gross_weight"] >= 15) & (items_df["units"] >= 10)])
print("")

print("multiple OR conditions")
print(items_df[(items_df["gross_weight"] >= 15) | (items_df["units"] >= 10)])
print("")

print("SQL-like BETWEEN/AND")
print(items_df[(items_df["gross_weight"] >= 15) & (items_df["gross_weight"] <= 16)])
print("")

print("SQL-like IN (...)")
print(items_df[items_df["item_code"].isin(["84500", "84400"])])
print("")

print("SQL-like wildcard match %text%")
print(items_df[items_df["item_description"].str.contains("SHORT")])
print("")

print("SQL-like wildcard match %text")
print(items_df[items_df["item_description"].str.startswith("COOKIE")])
print("")

print("SQL-like wildcard match text%")
print(items_df[items_df["item_description"].str.endswith("BAR")])
print("")

print("complex filter using masks - multiple BETWEEN/AND")
mask_min_weight = (items_df["gross_weight"] >= 15)
mask_max_weight = (items_df["gross_weight"] <= 16)
mask_min_units = (items_df["units"] > 10)
mask_max_units = (items_df["units"] < 25)
print(items_df[((mask_min_weight & mask_max_weight) | (mask_min_units & mask_max_units))])