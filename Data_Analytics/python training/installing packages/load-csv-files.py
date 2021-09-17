import pandas as pd

file_path = "C:/...the path to your file.../"

df_items = pd.read_csv(file_path + "items.csv")

print(df_items.head())