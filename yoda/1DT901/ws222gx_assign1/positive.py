user_input = int(input("Please provide an  integer: "))

# checks if the user input is positive or negative or neither
if (user_input > 0):
    print(user_input, "is positive")

elif (user_input < 0):
    print(user_input, "is negative")

else:
    print(user_input, "is neither positive nor negative")
