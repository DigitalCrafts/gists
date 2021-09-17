import pandas as pd

df_items = pd.read_csv("items.csv")
df_inventory_activity = pd.read_csv("inventory_activity.csv")

print(df_items.head())
print(df_inventory_activity.head())