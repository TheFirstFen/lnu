import random
import math


def pi_approx(n):

    points_inside_circle = 0

    # loop through number of points (n)
    for i in range(n):
        # generate a random point
        x = (random.uniform(-1, 1))
        y = (random.uniform(-1, 1))

        # check if the point is inside the circle
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            points_inside_circle += 1

    # return the pi approximation
    return (4 * (points_inside_circle / n))


n_values = [100, 10000, 1000000]
for i in n_values:
    pi = pi_approx(i)
    error = abs(math.pi - pi)
    print(f"for N={i} the pi approximation is: {pi} and the error is: {error}")
