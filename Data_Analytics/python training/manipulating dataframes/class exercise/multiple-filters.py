import pandas as pd

# declare file path and load csv as df
file_path = "C:/Users/mfcos/Desktop/full stack analytics/DigitalCrafts/trainings/Americold/python training/lessons/session-2/installing packages/"
items_df = pd.read_csv(file_path + "items_sample.csv")

# create TRUE/FALSE logical masks (optional but encouraged!)
mask_storage_type = (items_df["storage_type"] == "Freezer")
mask_weight = (items_df["gross_weight"] > 50)
mask_cube_min = (items_df["cube"] > 0.5)
mask_cube_max = (items_df["cube"] <= 1.0)

# filter items based on exercise requirements
filtered_items = items_df[mask_storage_type & (mask_weight | (mask_cube_min & mask_cube_max))]

# subset df columns
export_columns = ["item_code", "item_description", "storage_type", "gross_weight", "cube"]
filtered_items = filtered_items[export_columns]

# print first 5 lines of the filtered items then export
print(filtered_items.head())
filtered_items.to_csv("filtered_items.csv", index=False)