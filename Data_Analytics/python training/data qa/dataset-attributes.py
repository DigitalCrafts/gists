import pandas as pd

df_items = pd.read_csv("items_sample.csv")

print("INFO")
print(df_items.info())
print("")

print("DESCRIBE")
print(df_items.describe())
print("")

print("NUNIQUE")
print(df_items.nunique())
print("")
    
print("ITEM CODE VALUE COUNTS")
print(df_items["item_code"].value_counts())
print("")