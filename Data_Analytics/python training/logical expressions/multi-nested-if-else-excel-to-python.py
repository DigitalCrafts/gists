storage_type = "Freezer" # column E in Excel spreadsheet
tie = 8 # column F in Excel spreadsheet
high = 7 # column G in Excel spreadsheet

# column J in Excel spreadsheet
if storage_type == "Freezer":
    if tie*high <= 56:
        load_status = "OK to load"
    else:
        load_status = "Not enough space to load!"
else:
    load_status = "Not the right storage type!"