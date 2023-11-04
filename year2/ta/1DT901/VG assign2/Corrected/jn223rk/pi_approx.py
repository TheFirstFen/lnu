from random import random
from math import pi


# An implementaion of the Monte Carlo approximation of pi
def main():
    n = int(input("Enter how many points: "))
    points_in_quadrant = 0

    for i in range(n):
        x = random()
        y = random()
        if (x**2 + y**2 <= 1):
            points_in_quadrant += 1

    approx_pi = 4 * points_in_quadrant / n
    error_pi = ((approx_pi - pi) ** 2)**(1 / 2)
    print("Approximation of pi: {}".format(approx_pi))
    print("Actual value of pi correct to 15 decimals: {}"
          .format(pi))
    print("Error value: {}".format(error_pi))


if __name__ == "__main__":
    main()
