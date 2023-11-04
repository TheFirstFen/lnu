import random
import math


# calculates the distance between x and y values
def calc_distanc():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    calc_add = (x ** 2) + (y ** 2)
    calc_sqrt = math.sqrt(calc_add)

    return calc_sqrt


# finds the points for the circle in the correct parimeter
def find_points(N):
    points = 0

    for i in range(N):
        distance = calc_distanc()
        if distance <= 1:
            points += 1
    return points


area_of_square = 4
# loops through and calcualtes the approximation of pi and prints it
# prints the error between pi_apporx - pi
for r in range(1, 4):
    points = 0
    N = 100 ** r

    pi_approx = area_of_square*find_points(N) / N
    error = abs(math.pi - pi_approx)
    print(f"\nApproximation of π is {pi_approx}, when N is {N}")
    print("The error is", error)
