user_input_name = input("Enter a name: ")
user_input_place = input("Enter a place: ")

# welcome message with multiple values passed to string interpolation
welcome_message = "Hello, %s! Welcome to %s!" % (user_input_name, user_input_place)

print(welcome_message)