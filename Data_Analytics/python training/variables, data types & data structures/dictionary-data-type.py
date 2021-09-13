# create a dictionary 
item_dictionary = {
    "item_code":"71",
    "customer_name":"FROSTY TREATS",
    "item_description":"LEMON LIME BARS"
}

# get the item code value
print("the item_code is:", item_dictionary["item_code"])

# add a new key-value pair with the item's weight
item_dictionary["gross_weight"] = 5
print("updated item dictionary:", item_dictionary)

# get a list of the dictionary's keys
print("keys:", item_dictionary.keys())