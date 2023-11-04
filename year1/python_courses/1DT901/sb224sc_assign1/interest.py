'''Problem:
Write a program interest.py which computes the value of your savings S after Y years given a certain interest rate P (percentage).
You can assume that S, Y and P are integers. The value should be an integer correctly rounded off.
'''
'''Desired output examples:
Initial savings: 1000
Interest rate (in percentages): 9
Number of years: 5

The value of your savings after 5 years is: 1539
'''

# interest.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Computes the amount one would have after given years with a certain interest rate from a starting value
def interest_in_years(savings, rate, years):
    rate = (rate / 100) + 1
    interest = (savings * (rate ** years))
    interest = round(interest)
    return interest

# Reads input
savings = float(input('Initial savings: '))
rate = float(input('Interest rate (in percentages): '))
years = float(input('Number of years: '))

# Prints result from func interest_in_years
print(f'The value of your savings after {years} years is: ', interest_in_years(savings, rate, years))
