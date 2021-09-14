facility_ids = ["78401", "MO-SKSTN"]

facility_input = input("Enter a facility: ")
num_entries = 0
max_entries = 4

while (facility_input not in facility_ids) and (num_entries < max_entries):
    
    if facility_input not in facility_ids:

        facility_input = input("Facility invalid. Please try again: ")
        num_entries = num_entries + 1
    
    if num_entries == max_entries:
        print("Too many entries - try again some other time")