# distance.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

from math import sqrt


def distance(x1, y1, x2, y2):
    return round(sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)), 3)


x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

ans = distance(x1, y1, x2, y2)

print(
    f'The distance between ({x1},{y1}) and ({x2},{y2}) is {ans}')
