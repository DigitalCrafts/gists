import pandas as pd

file_path = "C:/Users/mfcos/Documents/GitHub/gists/"

df_items = pd.read_csv(file_path + "items.csv")

print(df_items.head())