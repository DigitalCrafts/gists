import pandas as pd

items_df = pd.read_csv("items_sample.csv")
cols = ["item_code", "item_description", "gross_weight", "unit_width"]

print("multiple AND conditons")
items_dff = items_df[(items_df["gross_weight"] >= 15) & (items_df["unit_width"] >= 10)]
print(items_dff[cols])
print("")

print("multiple OR conditions")
items_dff = items_df[(items_df["gross_weight"] >= 15) | (items_df["unit_width"] >= 10)]
print(items_dff[cols])
print("")

print("SQL-like BETWEEN/AND")
items_dff = items_df[(items_df["gross_weight"] >= 15) & (items_df["gross_weight"] <= 30)]
print(items_dff[cols])
print("")

print("SQL-like IN (...)")
items_dff = items_df[items_df["item_code"].isin(["item_code", "item_description", "gross_weight", "unit_width"])]
print(items_dff[cols])
print("")

print("SQL-like wildcard match %text%")
items_dff = items_df[items_df["item_description"].str.contains("CKN BST")]
print(items_dff[cols])
print("")

print("SQL-like wildcard match %text")
items_dff = items_df[items_df["item_description"].str.startswith("CKN")]
print(items_dff[cols])
print("")

print("SQL-like wildcard match %text")
items_dff = items_df[items_df["item_description"].str.endswith("CKN")]
print(items_dff[cols])
print("")

print("complex filter using masks - multiple BETWEEN/AND")
mask_min_weight = (items_df["gross_weight"] >= 20)
mask_max_weight = (items_df["gross_weight"] <= 40)
mask_min_units = (items_df["unit_width"] > 10)
mask_max_units = (items_df["unit_width"] < 25)
items_dff = items_df[(
    (mask_min_weight & mask_max_weight) | 
    (mask_min_units & mask_max_units)
)]
print(items_dff[cols])