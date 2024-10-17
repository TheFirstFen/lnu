# Importing math to be able to use sqrt
import math
# input from user
a = float(input("Enter a number: "))
# input from user
b = float(input("Enter a number: "))
# Input from user
c = float(input("Enter a number: "))
# Create a positive number under the sqrt
if (b**2) > (4*a*c) and a != 0:
    x = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    y = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    print("There are two solution, namely {} and {}".format(x, y))
    # Negative number under sqrt
elif (b**2) < (4*a*c) and a != 0:
    print("There is no solution")
else:
    # If a equals 0. only one solution can be made
    a == 0
    z = (-c/b)
    print("There is one solution, namely {}".format(z))
