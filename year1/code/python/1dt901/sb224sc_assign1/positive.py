'''Problem:
Write a program positive.py which reads an integer and then classifies (and prints) it as positive, zero, or negative.
'''
'''Desired output examples:
Please provide an integer: -27
-27 is negative
'''

# positive.py
# 
# Author: Samuel Berg
# Date: 27-Aug-2022

# Reads input
num = int(input('Please provide an integer: '))

# Computes whether or not the given integer is positive, negative or zero and prints result
if(num > 0):
    print(num, ' is positive')
elif(num < 0):
    print(num, ' is negative')
else:
    print(num, ' is zero')
