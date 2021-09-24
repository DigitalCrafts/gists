import pandas as pd

# read in the sample items csv as dataframe
items_df = pd.read_csv("items_sample.csv")

# user defined function to determine an item's category
def get_volume_category(item):

    # multiply width x height x depth to calculate volume
    volume = item["unit_width"]*item["unit_depth"]*item["unit_height"]

    if volume == 0:
        return "Missing data!"
    if volume < 2000:
        return "Small"
    if volume < 30000:
        return "Medium"
    else:
        return "Large"

# apply custom function to dataframe
# - the parameter "axis=1" indicates that an entire row will be the input to the function "apply_volume_category"
# - we apply "apply_volume_category" one row at a time, with the output of each function call creating the new column "volume_category"
items_df["volume_category"] = items_df.apply(get_volume_category, axis=1)

# define a list of columns to subset
# print dataframe including only these columns
subset_cols = ["item_code","item_description","unit_width","unit_depth", "unit_height","volume_category"]
print(items_df[subset_cols])