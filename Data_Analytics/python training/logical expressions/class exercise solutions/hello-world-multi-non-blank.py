user_input_name = input("Enter a name: ")
length_of_name = len(user_input_name)

if length_of_name > 0:
    user_input_place = input("Enter a place: ")
    length_of_place = len(user_input_place)
    if length_of_place > 0:
        message = "Hello, %s! Welcome to %s!" % (user_input_name, user_input_place)
    else:
        message = "Sorry, %s. We need a place to complete the welcome message :(" % user_input_name
else:
    message = "No name entered - cannot print welcome message :("

print(message)