import pandas as pd

file_path = "C:/...the path to your file.../"
export_file_path = "C:/...the path to export your file.../"

# load a csv file of items as a dataframe
df_items = pd.read_csv(file_path + "items.csv")

# ...some data manipulation steps...

# export final dataframe to a csv at the export_file_path
df_items.to_csv(export_file_path + "file_name.csv")