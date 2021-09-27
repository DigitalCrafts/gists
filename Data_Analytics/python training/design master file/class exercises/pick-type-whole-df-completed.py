import pandas as pd
import numpy as np

# read in sample data files from csv
df_items = pd.read_csv("items_sample.csv")
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")


def round_to_zero(number):

    if number < 0:
        rounded_number = np.ceil(number)
    else:
        rounded_number = np.floor(number)

    return int(rounded_number)


def get_picks(units, size):
    
    # get the number of full pallets/layers by dividing units by size
    num_picks = round_to_zero(units / size)

    # get the number of units picked
    units_picked = num_picks*size

    # get the number of units left to pick 
    units_remaining = units - units_picked

    return num_picks, units_picked, units_remaining


def get_all_pick_data(activity):

    # get the number of full pallet picks and units NOT picked on the full pallet
    full_pallet_picks, full_pallet_units, remaining_units = get_picks(units = activity["units"], size = activity["pallet_size"])

    # get the number of layer picks and units NOT picked on a layer
    if remaining_units != 0:
        layer_picks, layer_units, remaining_units = get_picks(units = remaining_units, size = activity["tie"])
    else:
        layer_picks = 0
        layer_units = 0
    
    # get the number cases picked by eaches
    if remaining_units != 0:
        case_picks = 1
    else:
        case_picks = 0

    # create a dictionary of the resulting pick type data
    activity_pick_data = {
        "full_pallet_picks":full_pallet_picks,
        "full_pallet_pick_units":full_pallet_units,
        "layer_picks":layer_picks,
        "layer_pick_units":layer_units,
        "case_picks":case_picks,
        "case_pick_units":remaining_units
    }

    return activity_pick_data



# filter items which only have a tie and high greater than 0
df_items = df_items[(df_items["tie"] > 0) & (df_items["high"] > 0)]
df_items["pallet_size"] = df_items["tie"] * df_items["high"]

# merge items & inventory_activity data single dataframe
df_item_activity = pd.merge(
    left = df_items, 
    right = df_inventory_activity,
    how = "inner",
    left_on = ["item_code","facility_id","customer_id"],
    right_on = ["item_code","facility_id","customer_id"]
)

pick_data_cols = df_item_activity.apply(get_all_pick_data, axis = 1, result_type='expand')
df_item_activity = pd.concat([df_item_activity, pick_data_cols], axis = 1)


cols = [
    "item_code",
    "item_description",
    "tie",
    "high",
    "billing_stack_qty",
    "pallet_size",
    "units",
    "full_pallet_picks",
    "full_pallet_pick_units",
    "layer_picks",
    "layer_pick_units",
    "case_picks",
    "case_pick_units"
]

# subset df by certain columns, print results, then save to df to a .csv file
df_item_activity = df_item_activity[cols]
print(df_item_activity)
df_item_activity.to_csv("item_activity_data.csv", index=False)