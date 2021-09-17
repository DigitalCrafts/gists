import pandas as pd

# set location of local file folder
file_path = "C:/...path to your file/"

# prompt user to enter a file name
file_to_load = input("Enter a file to load: ")

# conditional logic to load file based on user input
if file_to_load == "items":
    loaded_df = pd.read_csv(file_path + "/items_sample.csv")
    msg = loaded_df.head()

elif file_to_load == "inventory_activity":
    loaded_df = pd.read_csv(file_path + "/inventory_activity_sample.csv")
    msg = loaded_df.head()

else:
    msg = "File does not exist!"

# print out first 5 lines of the file or DNE message
print(msg)