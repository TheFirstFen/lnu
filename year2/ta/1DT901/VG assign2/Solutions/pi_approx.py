from math import sqrt, pi
from random import uniform

"""
inside   pi*R^2             4*inside
------ = -------  ==> pi =  --------
  N     (2R)^2                  N
"""


def inside_circle(x, y):
    return sqrt(x**2 + y**2) <= 1


def approx_pi(n):
    inside = 0
    for i in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if inside_circle(x, y):
            inside += 1
    pi_approx = 4*inside/n
    error = round(abs(pi_approx - pi), 5)
    return round(pi_approx, 5), error


# Program starts
print("\npi_approx", "error")

pi_approx, error = approx_pi(100)
print(pi_approx, error)

pi_approx, error = approx_pi(10000)
print(pi_approx, error)

pi_approx, error = approx_pi(1000000)
print(pi_approx, error)
