# Volume of a sphere with one decimal precision

# Read radius (a float)
r = float(input("Provide radius: "))

# Compute volume as V = 4*pi*r**3/3 + round off
pi = 3.141592653589793
a = 4*pi*r**3/3
a = round(a, 1)

print("The volume is", a)
