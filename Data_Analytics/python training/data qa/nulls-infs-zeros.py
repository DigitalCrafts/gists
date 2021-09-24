import pandas as pd
import numpy as np

df_items = pd.read_csv("items_sample.csv")

print("NULLS")
print(df_items.isnull().sum())
print("")

print("0's")
num_zeros = (df_items == 0).sum()
print(num_zeros)
print("")

print("INFs")
infs = df_items.isin([-np.inf,np.inf]).sum()
print(infs)
print("")