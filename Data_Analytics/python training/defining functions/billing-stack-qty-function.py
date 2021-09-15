# declare tie, high, and bsq
tie = 10
high = 5
bsq = 1

# define a function to calculate pallet size
def calculate_pallet_size(t, h, b):
    # multiply tie, high, and bsq
    ps = t * h * b
    # return pallet size so it can be used later in the program
    return ps

# set a variable called "pallet_size" to the output of the calculate_pallet_size function
pallet_size = calculate_pallet_size(tie, high, bsq)

# print the calculated pallet size to the console
print("The item's pallet size is %d" % pallet_size)