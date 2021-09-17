import pandas as pd

# file_path = "C:/...path to your file/"
file_path = "C:/Users/mfcos/Desktop/full stack analytics/DigitalCrafts/trainings/Americold/python training/lessons/session-2/installing packages"
file_to_load = input("Enter a file to load: ")

if file_to_load == "items":

    loaded_df = pd.read_csv(file_path + "/items_sample.csv")
    msg = loaded_df.head()

elif file_to_load == "inventory_activity":
    
    loaded_df = pd.read_csv(file_path + "/inventory_activity_sample.csv")
    msg = loaded_df.head()

else:
    msg = "File does not exist!"

print(msg)