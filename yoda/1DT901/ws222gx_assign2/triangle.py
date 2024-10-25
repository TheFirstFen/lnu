user_input = int(input("Enter an odd positive integer: "))

if user_input % 2 != 0 and user_input > 0:

    print("Right-Angled Triangle:")
    for i in range(user_input, 0, -1):
        print(" "*(user_input-i), "*"*(i))

    print("\nIsosceles Triangle:")
    for i in range(user_input-1, -1, -2):
        empty_space = " "*((i//2)+1)    # creates the empty space
        print(empty_space, "*"*(user_input-i))

else:
    print("Incorrect number for a triangle")
