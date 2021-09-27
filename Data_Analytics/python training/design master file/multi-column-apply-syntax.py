import pandas as pd

def my_custom_function(row):
    
    #...custom caclulations on reach row

    new_values = {
        "new_column_1_name":value_1,
        "new_column_2_name":value_2,
        #...and so on...
    }

    return new_values

original_df = pd.read_csv(#...reading csv to make a new df)

new_columns_df = original_df.apply(my_custom_function, axis = 1, result_type = "expand")
df_with_new_cols = pd.concat([original_df, new_cols_df], axis = 1)