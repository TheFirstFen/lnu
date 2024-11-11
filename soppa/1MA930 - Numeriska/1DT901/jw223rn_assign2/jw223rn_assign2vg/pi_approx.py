import random as rd
import math                     # Used to obtain the complete value of pi


# function that returns true if x, y is in or on the circle
def check_if_in(x, y):
    return (x ** 2) + (y ** 2) <= 1


# Main function that does the calculation for each number of points, n
def main(n):
    # Creating varaibles
    count = 1
    ins = 0
    while count <= n:           # Creates new points up until n amount
        x = rd.uniform(-1, 1)   # Creates random x coordinate
        y = rd.uniform(-1, 1)   # Creates random y coordinate
        if check_if_in(x, y):   # If point is in the circle adds 1 to ins
            count += 1
            ins += 1
        else:
            count += 1

    prop_in = ins / n           # Stores proportion of all points in circle
    app_pi = prop_in * 4        # Approximates pi
    return app_pi               # Returns the approximation of pi


# Executes the main function for n is equal to 1000, 10000 and 1000000
d100 = main(1000)
d10000 = main(10000)
d1000000 = main(1000000)

"""Prints the result of each n value calculated in main function, also prints
the difference from math.pi by printing the absolute value of the difference"""
print(f"The approximation of pi with 100 points is {d100} with an \
error of {abs(math.pi - d100)}")
print(f"The approximation of pi with 10000 points is {d10000} with an \
error of {abs(math.pi - d10000)}")
print(f"The approximation of pi with 1000000 points is {d1000000} with an \
error of {abs(math.pi - d1000000)}")
