import math

x1 = float(input("Enter the first x value: "))
y1 = float(input("Enter the first y value: "))
x2 = float(input("Enter the second x value: "))
y2 = float(input("Enter the second y value: "))

ans = math.sqrt((x1-x2)**2 + (y1-y2)**2)

p = "("
o = ")"
ra = round(ans, 3)
print(f'The distance between {p}{x1},{y1}{o} and {p}{x2},{y2}{o} is {ra} ')
