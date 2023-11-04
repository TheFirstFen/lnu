import random
import math


def approximate_pi(N):
    points_inside_circle = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = math.sqrt(x ** 2 + y ** 2)
        if distance <= 1:
            points_inside_circle += 1

    pi_approx = 4 * points_inside_circle / N
    pi_actual = math.pi
    error = abs(pi_actual - pi_approx)

    return pi_approx, error


# Calculate and print the approximation for N = 100
N = 100
approx, error = approximate_pi(N)
print(f"N = {N}: Approximation of pi = {approx}, Error = {error}")

# Calculate and print the approximation for N = 10000
N = 10000
approx, error = approximate_pi(N)
print(f"N = {N}: Approximation of pi = {approx}, Error = {error}")

# Calculate and print the approximation for N = 1000000
N = 1000000
approx, error = approximate_pi(N)
print(f"N = {N}: Approximation of pi = {approx}, Error = {error}")
