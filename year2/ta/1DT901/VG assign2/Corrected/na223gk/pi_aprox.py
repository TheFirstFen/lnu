import random
import math

def approximate_pi(N):
    inside_circle = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point (x, y) is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_approx = 4 * inside_circle / N
    return pi_approx

# Number of random points for approximation
N_values = [100, 10000, 1000000]

for N in N_values:
    pi_approx = approximate_pi(N)
    pi_actual = math.pi
    error = abs(pi_actual - pi_approx)

    print(f"For N = {N}:")
    print(f"Approximated π: {pi_approx}")
    print(f"Actual π: {pi_actual}")
    print(f"Error: {error}\n")

