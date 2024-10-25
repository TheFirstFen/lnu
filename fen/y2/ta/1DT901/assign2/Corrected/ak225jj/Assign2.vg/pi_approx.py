import random
from math import sqrt, pi

# area square
square = 4

for to_the_power in range(1, 4):
    n = 100 ** to_the_power
    tot_points = 0

    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        p = sqrt(x ** 2 + y ** 2)
        if -1 <= p <= 1:
            tot_points += 1
    approx_pi = (square * tot_points) / n   # print(tot_points)

    print(f"pi-approx = {approx_pi}")    # A * tp / n
    pi_actual = abs(pi - approx_pi)
    print(f"pi error value {pi_actual}")
