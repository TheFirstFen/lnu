from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


# Program starts
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

d = distance(x1, y1, x2, y2)
d = round(d, 3)

print(f"\nThe distance between ({x1},{y1}) and ({x2},{y2}) is {d}")
