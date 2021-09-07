storage_type = "Cooler" # column E in Excel spreadsheet

# column J in Excel spreadsheet
if storage_type == "Freezer":
    storage_temperature = "Coldest"
elif storage_type == "Cooler":
    storage_temperature = "Cold"
else:
    storage_temperature = "Not cold"