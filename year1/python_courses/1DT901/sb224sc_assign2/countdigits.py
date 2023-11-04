# countdigits.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

''' count_digits function:
Computes and keeps track of how many even, odd and zeros the given input had
and prints it to the screen
'''


def count_digits(N):
    zero = 0
    even = 0
    odd = 0
    for i in N:
        i = int(i)
        if i == 0:
            zero += 1
        elif i % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f'Zeros: {zero}')
    print(f'Odd: {odd}')
    print(f'Even: {even}')


# Takes input
N = input('Enter a large positive integer: ')

# Calls function count_digits() passing the input to it
count_digits(N)
