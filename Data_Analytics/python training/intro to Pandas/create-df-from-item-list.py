import pandas as pd

# create items (list of dictionaries)
items_list = [
    {
        'item_code': '84500', 
        'item_description': 'CHOCOLATE SHORTCAKE', 
        'customer_name': 'FROSTY TREATS', 
        'gross_weight': 15.95,
        'units':10
    }, 
    {
        'item_code':'84400', 
        'item_description':'STRAWBERRY SHORTCAKE', 
        'customer_name':'FROSTY TREATS',
        'gross_weight': 16.3,
        'units':15
    },
    {
        'item_code':8520,
        'item_description':'COOKIES & CREAM BAR', 
        'customer_name':'FROSTY TREATS',
        'gross_weight': 14.1,
        'units':25    
    }
]

# convert items into a df
items_df = pd.DataFrame(items_list)

print(items_df)