import random
import math

for j in range(1, 4):
    in_circle = 0
    n = 100**j
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        d = math.sqrt(x**2 + y**2)   # calculate distance from origin
        if d < 1:     # within the circle
            in_circle += 1

    # proportions
    b = in_circle / n

    # pi approximation
    pi_approx = b * 4

    # actual pi - pi_approx
    pi_error = abs(math.pi - pi_approx)

    print(f"\nWhen n is {n}, approx pi is:", pi_approx)
    print("Error:", pi_error)
