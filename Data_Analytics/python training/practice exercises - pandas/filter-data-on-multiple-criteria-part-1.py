import pandas as pd

# read in sample data files from csv
df_items = pd.read_csv("items_sample.csv")
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")

# prompt user for a storage type and date range
input_num_units = int(input("Enter a minimum number of units (press enter to skip): ")) * -1
input_storage_type = input("Enter a storage type: ")
print("")

# filter items and inventory_activity based on user input
df_items = df_items[df_items["storage_type"] == input_storage_type]
df_inventory_activity = df_inventory_activity[df_inventory_activity["units"] <= input_num_units]

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