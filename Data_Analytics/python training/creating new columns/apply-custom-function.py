import pandas as pd

# read in the sample items csv as dataframe
items_df = pd.read_csv("items_sample.csv")

# define a custom function which returns an item's storage temperate based on it's storage type
def get_storage_temp(item):

    storage_type = item["storage_type"]

    if storage_type == "Freezer":
        return "Coldest"
    elif storage_type == "Cooler":
        return "Cold"
    else:
        return "Not cold"

# apply custom function to dataframe
items_df["storage_temperature"] = items_df.apply(get_storage_temp, axis=1)

# specify a specific columns to display, then print the dataframe to the consol
subset_cols = ["item_code","item_description","storage_type","storage_temperature"]
print(items_df[subset_cols])