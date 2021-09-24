import pandas as pd

df_data = pd.DataFrame({
    "item_code":["431-432", "431-433", "431-434", "431-435", "431-436"],
    "tie":["5", "5", "10", "8", "7"],
    "high":[4, 4, 10, 7, 7]
})

print("Original data types")
print(df_data.dtypes)
print("")

# create a dictionary which is used to explicitly cast the data type of each column
# note: the dictionary below will cast every column's data type, however we can cast any number of columns at a time
col_data_types = {
    "item_code": "object",
    "tie":"int64",
    "high":"int64"
}

# cast each column to a new data type
df_data = df_data.astype(col_data_types)

print("New data types")
print(df_data.dtypes)