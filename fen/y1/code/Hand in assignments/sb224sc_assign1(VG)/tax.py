'''Problem:
In a (very) simplified version of the Swedish income tax system we have three tax levels depending on your monthly salary:

You pay a 30% tax on all income below 38.000 SEK/month
You pay an additional 5% tax on all income in the interval 38.000 SEK/month to 50.000 SEK/month
You pay an additional 5% tax on all income above 50.000 SEK/month

Write a program tax.py which reads a (positive) monthly income from the keyboard and then prints the corresponding income tax.
'''
'''Desired output examples:
Please provide monthly income: 32000
Corresponding income tax:  9600

Please provide monthly income: 46000
Corresponding income tax:  14200

Please provide monthly income: 79000
Corresponding income tax:  27200
'''

# tax.py
# 
# Author: Samuel Berg
# Date: 28-Aug-2022

# Computes the income tax one would have to pay in Sweden depending one ones monthly income
def calc_taxes(income) -> int:
    if (income > 50000):
        income_level_three = income % 50000
        income_tax_level_two = 12000 * 0.35
        income_tax_level_one = 38000 * 0.3
        income_tax_level_three = income_level_three * 0.4
        income_tax = income_tax_level_one + income_tax_level_two + income_tax_level_three
        return int(income_tax)
    elif (income > 38000 and income <= 50000):
        incomeLevelTwo = income % 38000
        income_tax_level_two = incomeLevelTwo * 0.35
        income_tax_level_one = 38000 * 0.3
        income_tax = income_tax_level_two + income_tax_level_one
        return int(income_tax)
    else:
        return int(income * 0.3)

# Reads input and makes sure it is valid
income = float(input('Please provide monthly income: '))
if (income < 0):
    exit()

# Prints result by calling func calc_taxes
print('Corresponding income tax: ', calc_taxes(income))
