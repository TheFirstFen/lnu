'''Problem:
Write a program oddpositive.py which generates a random number in the interval [-10,10] and classifies it as odd/even and as positive/negative.
Use the function random.randint in the random module. No reading from the keyboard in this exercise.  
'''
'''Desired output examples:
The generated number is -7
-7 is odd and negative

The generated number is 0
0 is even and neither positive nor negative
'''

# oddpositive.py
# 
# Author: Samuel Berg
# Date: 27-Aug-2022

# Importing random library to be able to get an random integer
import random

# Computes whether or not the random integer is positive or negative and if it is even or odd
def oddpositive(randInt):
    if (randInt > 0 and (randInt % 2) == 0):
        print(randInt, ' is even and positive')
    elif (randInt > 0 and (randInt % 2) != 0):
        print(randInt, ' is odd and positive')
    elif (randInt < 0 and (randInt % 2) == 0):
        print(randInt, ' is even and negative')
    elif (randInt < 0 and (randInt % 2) != 0):
        print(randInt, ' is odd and negative')
    else:
        print(randInt, ' is even and neither positive nor negative')

# Generates a random integer and prints it
randInt = random.randint(-10, 10)
print(f'The generated number is {randInt}')

# Calls func oddpositive
oddpositive(randInt)
