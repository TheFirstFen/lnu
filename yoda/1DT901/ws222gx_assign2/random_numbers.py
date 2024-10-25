import random

n = int(input("Enter number of integers to be generated: "))
num = 0
"""
sets number that are not realistic to be the largest number or the
smallest number
"""
max = -10
min = 1000
sum = 0


if num >= 1:
    print("\nGenerated values: ", end="")
    for i in range(n):
        """"
        assigns the random generated value to the value variable
        and prints it at the same time
        """
        print(value := random.randint(1, 100), end=" ")
        sum += value
        # checks if the value is bigger than the past max value
        if (value > max):
            max = value

        # checks if the value is smaller than the past min value
        elif (value < min):
            min = value

    # calculates the average
    avg = round(sum / n, 2)
    print(f"\nAverage, min, and max are {avg}, {min}, and {max}")

else:
    print("Invalid number, the number has to be positive")
