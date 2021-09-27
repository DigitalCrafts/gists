import pandas as pd
import numpy as np

# read in sample data files from csv
df_items = pd.read_csv("items_sample.csv")
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")


def round_to_zero(number):
    #...same as before...


def get_picks(units, size):
    #...same as before


def get_all_pick_data(#...your code here...):

    tie = #...your code here...
    high = #...your code here...
    units = #...your code here...

    # get the number of full pallet picks and units NOT picked on the full pallet
    full_pallet_picks, full_pallet_units, remaining_units = get_picks(#...your code here...)

    # get the number of layer picks and units NOT picked on a layer
    if remaining_units != 0:
        layer_picks, layer_units, remaining_units = get_picks(#...your code here)
    else:
        layer_picks = 0
        layer_units = 0
    
    # get the number cases picked by eaches
    if remaining_units != 0:
        case_picks = 1
    else:
        case_picks = 0

    #...same as befre...

# logic for applying multiple custom columns to a dataframe
pick_data_cols = df_item_activity.apply(get_all_pick_data, axis = 1, result_type='expand')
df_item_activity = pd.concat([df_item_activity, pick_data_cols], axis = 1)

# export df with pick type columns added to a csv file
df_item_activity.to_csv("item_activity_data.csv", index=False)