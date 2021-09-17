import pandas as pd

# create function to conditionally load a file
def load_file(file_path, file_to_load):

    # conditional logic to load file based on user input
    if file_to_load == "items":
        loaded_df = pd.read_csv(file_path + "/items_sample.csv")
        return loaded_df.head()

    elif file_to_load == "inventory_activity":
        loaded_df = pd.read_csv(file_path + "/inventory_activity_sample.csv")
        return loaded_df.head()

    else:
        return "File does not exist!"

# set location of local file folder
file_path = "C:/...path to your file/"

# prompt user to enter a file name
file_to_load = input("Enter a file to load: ")

# execute the load_file function using the user inputted file as input
loaded_df = load_file(file_to_load)

# print out first 5 lines of the file or DNE message
print(loaded_df)