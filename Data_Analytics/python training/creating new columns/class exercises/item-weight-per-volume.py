import pandas as pd
import numpy as np

# load sample items from .csv
items_df = pd.read_csv("items_sample.csv")

# filter for only items which contain "CKN" or "CHICKEN" in the description
items_df = items_df[items_df["item_description"].str.contains("CKN") | items_df["item_description"].str.contains("CHICKEN")]

# create "volume" column by multiplying width x height x depth --> round up using np.ceil()
items_df["volume"] = np.ceil(items_df["unit_width"] * items_df["unit_height"] * items_df["unit_depth"])

# create "weight_per_vol" by dividing gross_weight / volume --> round to 4 decimals
items_df["weight_per_volume"] = items_df["gross_weight"] / items_df["volume"]
items_df["weight_per_volume"] = items_df["weight_per_volume"].round(4)

# subset columns
export_columns = ["item_code", "item_description", "storage_type", "gross_weight", "volume", "weight_per_volume"]
items_df = items_df[export_columns]

# export to a csv without the index column
items_df.to_csv("weight_per_volume.csv", index=False)

print(items_df.head())