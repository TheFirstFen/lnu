# Import random and math module
import random
import math


# Checking if point is in circle
def is_in_circle_area(x, y):
    b = math.sqrt(1-x**2)  # Real y value for the unit circle
    a = -b  # Negative of the real y value for the unit circle
    if y > 0:
        if b > y:  # Comparing the real value with the value generated
            return True
        else:
            return False
    else:
        if a < y:  # Comparing the real value with the value generated
            return True
        else:
            return False


# Assigning x and y to random float values
def calc_pi(N):
    circle_counter = 0

    # Generate N random points between -1 and 1 and check if in circle
    for i in range(N):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if is_in_circle_area(x, y):
            circle_counter += 1

    # Calculation for pi
    pi = 4*circle_counter/(N)
    return pi


# Start of program

n_100 = calc_pi(100)

n_10000 = calc_pi(10000)

n_1000000 = calc_pi(1000000)

print(f"N = 100: {n_100}  Error: {math.pi-n_100}")
print(f"N = 10000: {n_10000}  Error: {math.pi-n_10000}")
print(f"N = 1000000: {n_1000000}  Error: {math.pi-n_1000000}")
