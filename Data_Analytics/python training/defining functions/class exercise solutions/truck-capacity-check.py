def calculate_item_weight(gross_weight, no_units):

    # calculate the item's total weight
    total_item_weight = gross_weight * no_units

    return total_item_weight


def truck_capacity_check(item_to_load_weight, current_weight, max_weight):

    # determine how much weight can be loaded onto a truck
    capacity_remaining = max_weight - current_weight

    # check if the truck can carry the weight of the material
    # - if yes --> truck has enough capacity
    # - if no --> truck does NOT have enough capacity
    if item_to_load_weight <= capacity_remaining:
        capacity_check = "OK to load"

    elif item_to_load_weight > capacity_remaining:
        capacity_check = "Not enough capacity!"

    return capacity_check


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

# list of trucks
truck_list = [
    {
        "truck_id":"TR0001",
        "current_weight":9900,
        "max_weight":10000
    },
    {
        "truck_id":"TR0002",
        "current_weight":1000,
        "max_weight":10000
    },
    {
        "truck_id":"TR0003",
        "current_weight":9700,
        "max_weight":10000
    }
]

# outer loop - iterate through all items in items_list
for item in items_list:

    # calcuate the weight of the current item
    weight_to_load = calculate_item_weight(item["gross_weight"], item["units"])
    
    # print the current item's description (use %s for string) and weight (using %d for float)
    print("Checking capacity for: %s; Total weight to load: %d" % (item["item_description"], weight_to_load))

    # inner loop - iterate through all trucks in truck_list
    for truck in truck_list:

        # determine if item can be loaded onto current truck
        load_status = truck_capacity_check(weight_to_load, truck["current_weight"], truck["max_weight"])

        # print out current truck (use %s for string) and result of the capacity check (use %s for string)
        print("%s: %s" % (truck["truck_id"], load_status))