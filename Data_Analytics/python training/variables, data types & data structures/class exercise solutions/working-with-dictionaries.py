# create item dictionaries
item_1 = {
    "item_code": "84500",
    "item_description": "CHOCOLATE SHORTCAKE",
    "customer_name": "FROSTY TREATS",
    "gross_weight": 15.95
}

item_2 = {
    "item_code": "84400",
    "item_description": "STRAWBERRY SHORTCAKE",
    "customer_name": "FROSTY TREATS",
    "gross_weight": 16.3
}

# create list of items and print to console
item_list = [item_1, item_2]
print("item_list:", item_list)

# get the weight of both items, add together, then print
total_item_weight = item_list[0]["gross_weight"] + item_list[1]["gross_weight"]
print("total_item_weight:", total_item_weight)