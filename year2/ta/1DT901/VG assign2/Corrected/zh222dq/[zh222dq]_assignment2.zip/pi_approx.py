import random as rn
import math


# Funktionen som beskriver vilka tal som är med i cirkeln
def in_circle(x, y):
    inside_circle = (math.sqrt(x**2 + y**2))
    if inside_circle <= 1:
        return True
    return False


# Start of program
N1 = 100
N2 = 10000
N3 = 1000000

# N = 100
# Antalet punkter i cirkeln
count = 0
for i in range(N1):
    x = rn.uniform(-1, 1)
    y = rn.uniform(-1, 1)
    if in_circle(x, y):
        count += 1

# Faktiska pi
pi_acutal_1 = math.pi
# Beräknar pi
pi_approx_1 = (4 * count)/N1
# Differensen
error_1 = pi_acutal_1-pi_approx_1


# N = 10000
count = 0
for i in range(N2):
    x = rn.uniform(-1, 1)
    y = rn.uniform(-1, 1)
    if in_circle(x, y):
        count += 1

pi_acutal_2 = math.pi
pi_approx_2 = (4 * count)/N2
error_2 = pi_acutal_2-pi_approx_2


# N = 1000000
count = 0
for i in range(N3):
    x = rn.uniform(-1, 1)
    y = rn.uniform(-1, 1)
    if in_circle(x, y):
        count += 1

pi_acutal_3 = math.pi
pi_approx_3 = (4 * count)/N3
error_3 = pi_acutal_3-pi_approx_3

print("N =", N1)
print("Pi approx:", pi_approx_1)
print("Pi acutal:", pi_acutal_1)
print("Error:", error_1)
print()
print("N =", N2)
print("Pi approx:", pi_approx_2)
print("Pi acutal:", pi_acutal_2)
print("Error:", error_2)
print()
print("N =", N3)
print("Pi approx:", pi_approx_3)
print("Pi acutal:", pi_acutal_3)
print("Error:", error_3)
