# import needed libraries
import random
from math import pi


# make function to check n dots inside square and find how many lands inside
# circle and how many lands outside (inside square).
def pi_approx(n):
    # set variables for calculations
    pi_actual = pi
    in_circle = 0
    square = 0

    # for loop that places n dots.
    for i in range(0, n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # call function to find distance from origo
        distance = distan(x, y)

        # check if outside circle
        if distance > 1:
            square += 1
        # if not in outside circle, then it's in :)
        else:
            in_circle += 1

    # calculate our approximate value of pi
    pi_approx = (in_circle / n) * 4

    # print results
    print(f"After {n} dots in the 2x2 square, {in_circle} landed inside the" +
          f" circle and {square} outside the circle")

    # print approximate value of pi
    print("These values would give us an approximate value of pi:" +
          f" {pi_approx} which is {(pi_actual - pi_approx)} different" +
          " from actual pi")


# make a funktion to find distance from center using pythagoras.
def distan(x, y):
    return (((x ** 2) + (y ** 2)) ** (1/2))


pi_approx(100)
pi_approx(10000)
pi_approx(1000000)
