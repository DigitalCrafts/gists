# import the numpy package and give it the alias np
import numpy as np

# creata a user defined function called round to zero
def round_towards_zero(number):

    # logical expression for rounding a number towards zero
    # - if number is less than zero (negative) round "up" towards zero
    # - otherwise, (if number is positive) round "down" towards zero
    if number < 0:
        rounded_number = np.ceil(number)
    else:
        rounded_number = np.floor(number)

    # cast rounded_number to an integer data type
    rounded_number = int(rounded_number)

    # return the final rounded number
    return rounded_number

# prompt a user to enter a number
# note: cast the number to a float during input
user_input_number = float(input("Enter a number: "))

# call the "round_towards_zero" function and use "user_input_number" as the input
rounded_number = round_towards_zero(user_input_number)

# print the final rounded number to the console log
print("rounded number: %d" % rounded_number)