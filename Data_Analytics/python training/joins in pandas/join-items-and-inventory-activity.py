import pandas as pd
from pandas.core.reshape.merge import merge

# load items and inventory_activity from csv
file_path = "C:/...the path to your file.../"
df_items = pd.read_csv(file_path + "items_sample.csv")
df_inventory_activity = pd.read_csv(file_path + "inventory_activity_sample.csv")

print(df_items.head())
print(df_inventory_activity.head())

# merge them into a single dataframe
merged_df = pd.merge(
    left = df_items, 
    right = df_inventory_activity,
    how = "inner",
    left_on = ["item_code","facility_id","customer_id"],
    right_on = ["item_code","facility_id","customer_id"]
)

# print the first few rows and column headers
print(merged_df.head())
print(merged_df.columns)
print(merged_df.shape)