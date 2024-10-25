import random
import math


# Generate random points and check how many falls inside the
def approx_pi(n):
    number_of_points = n
    inside_circle = 0
    for rand in range(number_of_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle/n)*4
    return error_rate(pi_approx, n)


# calculate the error rate by comparing the result
#  from approx_pi with pi in math
def error_rate(pi_approx, n):
    error = abs(math.pi - pi_approx)
    print(f"Estimeted value of pi {pi_approx} - the real pi value π givs us \
the error rate {error}\n the amunt of random point used {n} ")


test_value = [10, 100, 10000, 1000000]
for x in test_value:
    approx_pi(x)
