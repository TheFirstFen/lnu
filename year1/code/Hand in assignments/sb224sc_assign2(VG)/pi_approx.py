# pi_approx.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022

# Importing pi from math for actual PI and uniform from random
# for random point generation
from math import pi
from random import uniform

''' pi_approx function:
Takes an amount N of points it will use to compute actual PI
for each generated point sends it to in_unit_circle function
if it is in the unit circle then adds it to the list of points
otherwise generates a new point.
when finished generating and checking N points then computes
an approximate of PI by using the formula
(squareArea * (amount of points in unit circle / N generated points))
and prints the result and difference between actual PI and approximated PI
'''


def pi_approx(N):
    # Creates a list to store all the appropriate points in
    points = []
    for _ in range(N):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if (in_unit_circle(x, y)):
            points.append([x, y])
    approx = SQUARE_AREA * (len(points) / N)
    print(f'PI is approximately: {approx}')
    print(f'Difference between actual pi and approximated: {abs(pi - approx)}')


''' in_unit_circle function:
Checks with the help of a^2 + b^2 = c^2 if a point is within the circle
if it is within the circle then it returns True otherwise False
'''


def in_unit_circle(x, y):
    if x ** 2 + y ** 2 <= RADIUS:
        return True
    else:
        return False


# Creates to constants
RADIUS = 1
SQUARE_AREA = 4

# Computes
pi_approx(100)
pi_approx(10000)
pi_approx(1000000)
