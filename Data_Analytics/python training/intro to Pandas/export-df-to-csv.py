import pandas as pd

# load a csv file of items as a dataframe
df_items = pd.read_csv("items.csv")

# ...some data manipulation steps...

# export final dataframe to a csv at the export_file_path
df_items.to_csv("file_name.csv")