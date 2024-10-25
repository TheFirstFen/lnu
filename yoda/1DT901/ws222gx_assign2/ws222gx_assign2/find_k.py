user_input = int(input("Enter a positive integer: "))

if (user_input > 0):
    sum = 0
    k = 1
    """
    loops through until the sum of (sum and k) is less or equal to user_input
    which gives the smallest k value -2 due to it checks when it is over the
    user_input variable
    """
    while (sum <= user_input):
        sum += k
        k += 2

    print(k-2, "is the smallest k such that 1+3+5+...+k > ", user_input)

    sum = 0
    k = 2
    """
    loops through until the sum of (sum and k) is over user input
    which gives the largest k value -2
    """
    while (sum + k <= user_input):
        sum += k
        k += 2

    print(k-2, "is the largest k such that 0+2+4+6+...+k < ", user_input)

else:
    print("The integer is not a positive number:", user_input)
