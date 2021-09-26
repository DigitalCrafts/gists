import pandas as pd


# read in sample data files from csv
df_items = pd.read_csv("items_sample.csv")
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")


def filter_storage_type_check(storage_type, valid_storage_types, default_storage_type = "Freezer"):

    # check if entered storage type is "valid" --> will be valid if:
    # - storage_type is in list of valid_storage_types
    # - storage_type is a blank string (ie, user presses "enter")
    if storage_type in valid_storage_types:
        return storage_type
        
    elif storage_type == "":
        return default_storage_type
    
    else:
        # initiate number of re-entered storage type attempts and incremental variable
        num_attempts = 0
        max_attempts = 5
        while num_attempts < max_attempts:

            # prompt user to re-enter a storage type
            re_entered_storage_type = input("Storage type invalid! Please try again (press enter to skip): ")

            # determine if re-entered storage type is valid
            if re_entered_storage_type in valid_storage_types:
                return re_entered_storage_type
            elif re_entered_storage_type == "":
                return default_storage_type

            # increment the number of attempts by 1 after each iteration
            num_attempts = num_attempts + 1
        
        # if too many attempts --> notify user and do not filter by storage type
        print("Too many attempts! Using default storage type")
        return default_storage_type


def num_units_check(num_units):

    if num_units == "":
        return 0
    else:
        return int(num_units)*-1


# get user input for number of units and filter activities
# - if user skips entry --> default to 0 units
# - otherwise, filter by number of entered units
input_num_units = input("Enter a minimum number of units (press enter to skip): ")
input_num_units = num_units_check(input_num_units)
df_inventory_activity = df_inventory_activity[df_inventory_activity["units"] <= input_num_units]


# filter items and inventory_activity based on user input
input_storage_type = input("Enter a storage type (press enter to skip): ")
input_storage_type = filter_storage_type_check(input_storage_type, ["Dry", "Freezer", "Cooler"])
df_items = df_items[df_items["storage_type"] == input_storage_type]
print("")


# filtered items and inventory_activity df's into a single df
df_item_activity = pd.merge(
    left = df_items, 
    right = df_inventory_activity,
    how = "inner",
    left_on = ["item_code","facility_id","customer_id"],
    right_on = ["item_code","facility_id","customer_id"]
)

# specifiy columns to export and export file name
export_cols = ["item_code","item_description","customer_name","storage_type","activity_type","units","filter_date"]
export_file_name = input_storage_type + "_item_activity.csv"

# print first few lines of final dataset and export
print(df_item_activity[export_cols])
df_item_activity[export_cols].to_csv(export_file_name, index = False)