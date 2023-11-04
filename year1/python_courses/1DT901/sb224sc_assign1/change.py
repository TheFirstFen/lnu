'''Problem:
Write a program change.py that computes the change a customer should receive when she/he has paid a certain sum.
The program should exactly describe the minimum number of Swedish bills and coins that should be returned rounded off to nearest krona (kr). 
'''
'''Desired output examples:
Price: 372.38
Payment: 1000

Change: 628 kr
1000kr bills: 0
 500kr bills: 1
 200kr bills: 0
 100kr bills: 1
  50kr bills: 0
  20kr bills: 1
  10kr coins: 0
   5kr coins: 1
   2kr coins: 1
   1kr coins: 1
'''

# change.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Computes how many of each bill/coin shall be given to customer and prints it
def calc_change(total_change):
        for i in [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]:
                space = ' ' * (4 - (len(str(i))))               # Computes amount of spaces in front of each bill/coin
                type_currency = 'bills:' if i > 10 else 'coins:'
                print(f'{space}{i}kr {type_currency} {total_change // i}')
                total_change %= i

# Reads input
total_price = float(input('Price: '))
amount_payed = float(input('Payment: '))

# Computes the change
total_change = int((amount_payed - round(total_price)))
print(f'Change: {total_change}')

# Calls  func calc_change the computes and prints result
calc_change(total_change)
