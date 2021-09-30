import pandas as pd


df = pd.DataFrame("...read in raw data from csv/SQL")

# sort the dataframe
df = df.sort_values(by='customer_id')

# filter df for only LTL orders
df = df[df["truckload"] == "LTL"]

# get a list of customer ids
cust_ids = df["customer_id"].unique().tolist()

# set up columns and aggregation setup
cols = ["customer_id","week","year","zip_3","gross_weight","cust_ref_num"]
agg_groupby = ["week","year","zip_3","customer_id"]
agg_setup = {
    "gross_weight":"sum",
    "cust_ref_num":"count"
}


# loop through list of customer ids
# 1) create a df of just of the current customer (df_c)
# 2) create a df of all customer except the current customer (df_not_c)
# 3) aggregate both df's, summing the weight and getting an order count
# 4) inner join both df's on matching zips, years, and weeks 
#   --> more than 0 rows == consolidation opportunity
# 5) append merged df's with consolidation opportunities to a list

consol_opps_df_list = []
for c in cust_ids:

    df_c = (df
        .loc[df["customer_id"] == c][cols]
        .groupby(agg_groupby)
        .agg(agg_setup)
        .reset_index()
    )
    df_not_c = (df
        .loc[df["customer_id"] != c][cols]
        .groupby(agg_groupby)
        .agg(agg_setup)
        .reset_index()
    )

    df_consol = pd.merge(
        left = df_not_c,
        right = df_c,
        how = "inner",
        left_on=["week","year","zip_3"],
        right_on=["week","year","zip_3"]
    )
    
    if df_consol.shape[0] > 0:
        consol_opps_df_list.append(df_consol)
    else:
        print("No consolidation opportunities for %s" % c)

# if there are consolidation opps...
if len(consol_opps_df_list) > 0:
    
    # append all df's into a single df
    consol_ops_df = pd.concat(consol_opps_df_list)
    
    # aggregate df to get total weight and orders for each customer combo
    consol_ops_df = (consol_ops_df
        .groupby(["customer_id_x","customer_id_y"])
        .agg({
            "gross_weight_x":"sum",
            "gross_weight_y":"sum",
            "cust_ref_num_x":"sum",
            "cust_ref_num_y":"sum"
        })
        .reset_index()
    )

    # change the sign of gross weight columns
    consol_ops_df["gross_weight_x"] = consol_ops_df["gross_weight_x"] * -1
    consol_ops_df["gross_weight_y"] = consol_ops_df["gross_weight_y"] * -1

    # rename report based on columns defined in the setup dictionary
    consol_ops_df.columns = [
           "customer_id_x",
           "customer_id_x",
           "gross_weight_x",
           "gross_weight_y",
           "cust_ref_num_x",
           "cust_ref_num_y"
       ]

    # export final report to a csv file
    print(consol_ops_df)
    consol_ops_df.to_csv("consolidation_opportunities.csv")

else:
    print("No consolidation opportunities found!") 

