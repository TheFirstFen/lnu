import random as rd
import math


# function for approximating pi
def aprox_pi(num):
    inside = 0
    for _ in range(num):
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)
        distance = math.sqrt(x**2 + y**2)  # Distance = √(x² + y²)
        if distance <= 1:
            inside += 1  # Count only points inside the circle
    pi = inside / num * 4  # Approximate pi based on the ratio of points
    return pi              # inside the circle


# Testing list
lst_num = [100, 10000, 1000000]
# Loop through the list
for n in lst_num:
    pi_actual = math.pi  # Actual value of pi
    pi_aprox = aprox_pi(n)  # Get approxi pi
    pi_dif = abs(pi_actual - pi_aprox)  # Calculate the error
    print(f"N = {n}\n"
          f"Approximated pi: {pi_aprox}\n"
          f"Actual pi: {pi_actual }\n"
          f"Error: {pi_dif}\n")
