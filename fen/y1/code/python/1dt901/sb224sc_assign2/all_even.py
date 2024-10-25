# all_even.py
#
# Author: Samuel Berg
# Date: 01-Sep-2022

# Computes the sum of all the even number <= 100
sum = 0
for i in range(101):
    if (i % 2 == 0):
        sum += i

# Prints result
print(f'Sum of the 100 first numbers is: {sum}')
