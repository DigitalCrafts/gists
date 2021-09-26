import pandas as pd

# load inventory_activity from csv
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")

# create dictionary of how each column will be aggregated
agg_setup = {
    "item_code":"count",
    "units":"sum"
}

# aggregate inventory activity data using agg_setup
dfg_inventory_activity = df_inventory_activity.groupby("item_code").agg(agg_setup)

# view aggregated data in console
print(dfg_inventory_activity)