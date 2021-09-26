import pandas as pd

# load inventory_activity from csv
df_inventory_activity = pd.read_csv("inventory_activity_sample.csv")

# create dictionary of how each column will be aggregated
agg_setup = {
    "item_code":"nunique",
    "units":'sum'
}

# aggregate inventory activity data using agg_setup
dfg_inventory_activity = df_inventory_activity.groupby("filter_date").agg(agg_setup).reset_index()

print(dfg_inventory_activity)