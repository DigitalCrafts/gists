import pandas as pd

file_path = "C:/...path to your file/"

df_items = pd.read_csv(file_path + "items_sample.csv")
df_inventory_activity = pd.read_csv(file_path + "inventory_activity_sample.csv")

print("Items sample")
print(df_items.head())

print("Inventory activity sample")
print(df_inventory_activity.head())