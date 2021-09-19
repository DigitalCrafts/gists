import pandas as pd
import numpy as np

# load sample items from .csv
file_path = "C:/Users/mfcos/Desktop/full stack analytics/DigitalCrafts/trainings/Americold/python training/lessons/session-2/installing packages/"
items_df = pd.read_csv(file_path + "items_sample.csv")

# add new columns using np functions floor/ceil
items_df["gross_weight_rounded_down"] = np.floor(items_df["gross_weight"])
items_df["gross_weight_rounded_up"] = np.ceil(items_df["gross_weight"])

print(items_df)