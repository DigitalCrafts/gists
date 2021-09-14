# define list of valid facility IDs
facility_ids = ["78401", "MO-SKSTN"]

# get user input of facility ID
facility_input = input("Enter a facility ID: ")

# set up criteria for while loop
num_entries = 0
max_entries = 4

# prompt user for a facility until either:
# 1) user enters a valid facility
# 2) user exceeds max number of entries
while (facility_input not in facility_ids) and (num_entries < max_entries):
    
    facility_input = input("Facility ID invalid. Please try again: ")
    num_entries = num_entries + 1
    
    if num_entries == max_entries:
        print("Too many entries - try again some other time")