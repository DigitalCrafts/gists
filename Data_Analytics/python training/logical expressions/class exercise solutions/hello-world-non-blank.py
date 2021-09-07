user_input_name = input("Enter a name: ")
user_input_place = input("Enter a place: ")

if user_input_name == "":
    message = "No name entered - cannot print welcome :("
else:
    # welcome message with multiple values passed to string interpolation
    message = "Hello, %s! Welcome to %s!" % (user_input_name, user_input_place)

print(message)