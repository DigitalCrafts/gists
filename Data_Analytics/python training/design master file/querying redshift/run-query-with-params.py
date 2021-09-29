import pandas as pd

# import locally stored functions and scripts
import sql_queries
from connect_to_db import connect_to_db

# set query parameters
facility_id = ["78401"]
customer_id = ["91525"]
start_date = '2021-01-01'
end_date = '2021-12-31'

# create parameter dictionary
query_filters = {
    "customer_id_list":tuple(customer_id),
    "facility_id_list":tuple(facility_id),
    "start_date":start_date,
    "end_date":end_date
}

# specify a query to run
query = sql_queries.ITEM_ACTIVITY

# execute query against the database
data = connect_to_db(query, query_filters)

# convert data to a df
df = pd.DataFrame(data)

# rename columns
df.columns = [
    "facility_id",
    "item_code",
    "item_description",
    "item_family",
    "storage_type",
    "unit_depth",
    "unit_width",
    "unit_height",
    "gross_weight",
    "tie",
    "high",
    "billing_stack_qty",
    "units"
]

# print first few lines of the df
print(df.head())

# export dataframe to a csv
df.to_csv("queried_data.csv", index=False)