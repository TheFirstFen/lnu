import math


# uses the distance formula to calculate the distance
def distance(x1, y1, x2, y2):
    # distance = Sqrt( (x1-x2)^2 + (y1-y2)^2 )
    dx_squared = (x1-x2)**2
    dy_squared = (y1-y2)**2
    sqrt = math.sqrt((dx_squared + dy_squared))
    return round(sqrt, 3)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dis = distance(x1, y1, x2, y2)

print(f"The distance between {x1, y1} and {x2, y2} is {dis}")
