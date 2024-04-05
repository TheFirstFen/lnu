'''Problem:
Write a program largest.py which reads three integers A, B, C and then prints the largest number.
You should solve this problem using if statements.
You are not allowed to use any of the max and sort functions that comes with Python.
'''
'''Desired output examples:
Please provide three integers A, B, C.
Enter A: 23
Enter B: 46
Enter C: -11

The largest number is: 46
'''

# largest.py
# 
# Author: Samuel Berg
# Date: 27-Aug-2022

# Computes which of the three given numbers is the largest
def largest_num(num_a, num_b, num_c):
    if(num_a > num_b and num_a > num_c):
        return num_a
    elif(num_b > num_a and num_b > num_c):
        return num_b
    else:
        return num_c

# Requests & reads input
print('Please provide three integers A, B, C.')
num_a = int(input('Enter A: '))
num_b = int(input('Enter B: '))
num_c = int(input('Enter C: '))

# Prints result
print('The largest number is: ', largest_num(num_a, num_b, num_c))
