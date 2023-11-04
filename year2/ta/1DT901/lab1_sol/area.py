# Area of a circle with one decimal precision

# Read radius (a float)
r = float(input("Provide radius: "))

# Compute area as A = pi*r*r + round off
pi = 3.141592653589793
a = pi*r*r
a = round(a, 1)

print("Corresponding area is", a)
