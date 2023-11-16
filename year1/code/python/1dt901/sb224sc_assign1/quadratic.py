''' Problem:
You can solve quadratic equations using the quadratic formula.
Quadratic equations are of the form Ax^2 + Bx + C = 0.
Such equations have zero, one or two solutions. 
The first solution is (-B + sqrt ( B2 - 4AC ))/(2A ).
The second solution is (-B - sqrt( B 2 - 4AC )) / ( 2A).
There are no solutions if the value under the square root is negative.
There is one solution if the value under the square root is zero.
Write a program that asks the user for the values of A, B, and C, then reports whether there are zero, one, or two solutions, then prints those solutions.
Note: Make sure that you also take into account the case that A is zero (there is only one solution then, namely - C/B), and the case that both A and B are zero.
'''
'''Desired output examples:
A: 1.5
B: 1
C: 0.1
There are two solutions, namely -0.1225148226554414 and -0.5441518440112253

A: 5
B: 3
C: 3
There are no solutions

A: 5
B: 6
C: 1
There are two solutions, namely -0.2 and -1.0
'''

# quadratic.py
# 
# Author: Samuel Berg
# Date: 28-Aug-2022

# Importing sqrt from the math library to be able to get the square root of a value 
from math import sqrt

# Computes the root(s) of an given equation and how many there are
def quadratic_equation(num_a, num_b, num_c):
    discriminant = num_b * num_b - 4 * num_a * num_c
    
    if(num_a == 0 and num_b != 0):
        root1 = root2 = -num_c/num_b
        print(f'There is one solution, namely {root1}')
    elif(num_a == 0 and num_b == 0):
        print('There are no solutions')
    else:
        if(discriminant > 0):
            root1 = (-num_b + sqrt(discriminant)) / (2 * num_a)
            root2 = (-num_b - sqrt(discriminant)) / (2 * num_a)
            print(f'There are two solutions, namely {root1} and {root2}')
        elif(discriminant == 0):
            root1 = root2 = -num_b / (2 * num_a)
            print(f'There is one solution, namely {root1}')
        elif(discriminant < 0):
            print('There are no solutions')

# Reads input
num_a = float(input('A: '))
num_b = float(input('B: '))
num_c = float(input('C: '))

# Calls func quadratic_equation
quadratic_equation(num_a, num_b, num_c)

