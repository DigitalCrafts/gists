import pandas as pd
import numpy as np

# read in sample data files from csv
df_items = pd.read_csv("items_sample.csv")
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")

# create a user defined function which rounds the pallet picks of each activity record
def get_num_pallets(activity):

    # set the pallet size and units equal to the pallet_size and units from the activity
    pallet_size = activity["pallet_size"]
    units = activity["units"]

    # get the number of pallets by dividing units by pallet size
    num_pallets = units / pallet_size

    # if num_pallets is less than zero --> round up; if num_pallets is greater than zero --> round down
    if num_pallets < 0:
        rounded_num_pallets = np.ceil(num_pallets)
    else:
        rounded_num_pallets = np.floor(num_pallets)

    return int(rounded_num_pallets)


# filter items which only have a tie and high greater than 0
df_items = df_items[(df_items["tie"] > 0) & (df_items["high"] > 0)]

# merge sample data into a single dataframe
# - use an inner join on matching rows
# - join on matching item_code, facility_id, customer_id
df_item_activity = pd.merge(
    left = df_items, 
    right = df_inventory_activity,
    how = "inner",
    left_on = ["item_code","facility_id","customer_id"],
    right_on = ["item_code","facility_id","customer_id"]
)

# create a new column called pallet_size which is the product of tie x high
df_item_activity["pallet_size"] = df_item_activity["tie"] * df_item_activity["high"]

# use the apply function to evaluate how many full pallets were selected for each activity
# specifying axis = 1 the entire dataframe, one activity at a time
df_item_activity["full_pallet_picks"] = df_item_activity.apply(get_num_pallets, axis = 1)
print(df_item_activity[["item_code","item_description","facility_id","customer_id","filter_date", "tie", "high", "activity_type","units","pallet_size","full_pallet_picks"]])