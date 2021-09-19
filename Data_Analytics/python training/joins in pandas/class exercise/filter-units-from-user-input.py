import pandas as pd

# load items and inventory_activity from csv
file_path = "C:/...the path to your file.../"
df_items = pd.read_csv(file_path + "items_sample.csv")
df_inventory_activity = pd.read_csv(file_path + "inventory_activity_sample.csv")


def get_min_units(user_input):
    # check user input value
    # - return 0 if nothing entered
    # - return the input value otherwise
    if user_input == "":
        return 0
    else:
        return int(user_input)


def merge_datasets(items_data, inventory_activity_data, merge_columns):
    # merge items and inventory activity data
    merged_df = pd.merge(
        left = items_data, 
        right = inventory_activity_data,
        how = "inner",
        left_on = merge_columns,
        right_on = merge_columns
    )

    return merged_df


def filter_activity_data(activity_data, min_units):
    # filter units based on the user input
    filtered_data = activity_data[activity_data["units"] > min_units]

    return filtered_data


# define columns to merge dataset on
merge_columns = ["item_code","facility_id","customer_id"]

# prompt user for a minimum number of units
user_input = input("Enter min units: ")
min_units = get_min_units(user_input)

# filter activity data based on user input
df_inventory_activity = filter_activity_data(df_inventory_activity, min_units)

# merged filtered activity data and items data into a single dataframe
merged_df = merge_datasets(df_items, df_inventory_activity, merge_columns)

# print the first few rows and column headers
print(merged_df)
print(merged_df.columns)
print(merged_df.shape)