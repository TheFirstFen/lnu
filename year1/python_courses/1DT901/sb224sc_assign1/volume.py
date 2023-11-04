'''Problem:
Create a program volume.py that asks for the radius of a sphere and prints the volume.
The result should be presented with a single decimal correctly rounded off.
'''
'''Desired output examples:
Provide a radius: 6
The volume is 904.8
'''

# volume.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Importing pi from math library to be able to get the value of pi
from math import pi

# Computes the volume of a sphere with a given radius
def sphere_volume(radius):
    return (4/3) * pi * (radius ** 3)

# Reads input
radius = float(input('Provide a radius: '))

# Prints result by calling func sphere_volume
print('The volume is ', round(sphere_volume(radius), 1))
