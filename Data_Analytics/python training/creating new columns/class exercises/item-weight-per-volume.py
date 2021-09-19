import pandas as pd
import numpy as np

# load sample items from .csv
file_path = "C:/...path to your file.../"
items_df = pd.read_csv(file_path + "items_sample.csv")

# filter for only items which contain "CKN" or "CHICKEN" in the description
items_df = items_df[items_df["item_description"].str.contains("CKN") | items_df["item_description"].str.contains("CHICKEN")]

# create "volume" column by multiplying width x height x depth --> round up using np.ceil()
items_df["volume"] = np.ceil(items_df["unit_width"] * items_df["unit_height"] * items_df["unit_depth"])

# create "weight_per_vol" by dividing gross_weight / volume --> round to 4 decimals
items_df["weight_per_vol"] = items_df["gross_weight"] / items_df["volume"]
items_df["weight_per_vol"] = items_df["weight_per_vol"].round(4)