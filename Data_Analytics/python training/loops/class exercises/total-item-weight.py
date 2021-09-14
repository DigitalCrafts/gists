# list of items
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

# declare variable to store total weight
total_weight = 0

# loop through all items in items_list
for item in items_list:

    # multiply an units x gross weight to get the item weight
    # note: each item is a dictionary --> access values by indexing with a key
    item_weight = item['gross_weight'] * item['units']

    # print the current item description and weight to the console
    # note: use "%s" as a placeholder for the item description (a string) and "%d" as a placeholder for the item weight (a float)
    print("Item: %s, Item weight on hand: %d" % (item["item_description"], item_weight))

    # increment total weight with current item's weight
    total_weight = total_weight + item_weight

# finally, print the total weight of all items
print("Total weight of all items: %d" % total_weight)
