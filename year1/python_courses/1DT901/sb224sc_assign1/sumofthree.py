'''Problem:
Write a program sumofthree.py which asks the user to provide a three digit number. The program should then compute the sum of the three digits.
Note: you may not convert the input from an integer to a string or a list (or anything else), you need to calculate the answer. 
'''
'''Desired output examples:
Provide a three digit number: 456
Sum of digits: 15
'''

# sumofthree.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Computes the sum of an given integers digits and returns it
def calc_sum_of_three(variable) -> int:
    sum_of_three = 0
    while(variable > 0):
        sum_of_three += variable % 10
        variable = variable // 10
    return sum_of_three

# Reads input
variable = int(input('Provide a three digit number: '))

# Prints result by calling func calc_sum_of_three
print('Sum of digits: ', calc_sum_of_three(variable))
