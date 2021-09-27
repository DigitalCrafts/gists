import pandas as pd
import numpy as np


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

    # get number of lines
    if num_picks == 0:
        num_lines = 0
    elif num_picks < 0:
        num_lines = -1
    else:
        num_lines = 1

    return num_picks, num_lines, units_picked, units_remaining


def get_all_pick_data(tie, high, num_units):

    # get the number of full pallet picks and units NOT picked on the full pallet
    full_pallet_picks, full_pallet_lines, full_pallet_units, remaining_units = get_picks(units = num_units, size = tie*high)

    # get the number of layer picks and units NOT picked on a layer
    if remaining_units != 0:
        layer_picks, layer_lines, layer_units, remaining_units = get_picks(units = remaining_units, size = tie)
    else:
        layer_picks = 0
        layer_lines = 0
        layer_units = 0
    
    # get the number cases picked by eaches
    if remaining_units == 0:
        case_picks = 0
        case_lines = 0
    elif remaining_units < 0:
        case_picks = -1
        case_lines = -1
    else:
        case_picks = 1
        case_lines = 1

    # create a dictionary of the resulting pick type data
    activity_pick_data = {
        "full_pallet_picks":full_pallet_picks,
        "full_pallet_units":full_pallet_units,
        "full_pallet_lines":full_pallet_lines,
        "layer_picks":layer_picks,
        "layer_units":layer_units,
        "layer_lines":layer_lines,
        "case_picks":case_picks,
        "case_units":remaining_units,
        "case_lines":case_lines
    }

    return activity_pick_data

# example activity data
tie = 20
high = 10
num_units = 227

pick_type_data = get_all_pick_data(tie, high, num_units)
print("PICKING DATA")
print("Full pallet picks: %d" % pick_type_data["full_pallet_picks"])
print("Full pallet lines: %d" % pick_type_data["full_pallet_lines"])
print("Full pallet qty: %d" % pick_type_data["full_pallet_units"])
print("Layer picks: %d" % pick_type_data["layer_picks"])
print("Layer lines: %d" % pick_type_data["layer_lines"])
print("Layer qty: %d" % pick_type_data["layer_units"])
print("Case picks: %d" % pick_type_data["case_picks"])
print("Case lines: %d" % pick_type_data["case_lines"])
print("Case qty: %d" % pick_type_data["case_units"])