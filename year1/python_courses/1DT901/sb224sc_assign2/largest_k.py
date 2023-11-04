# largest_k.py
#
# Author: Samuel Berg
# Date: 01-Sep-2022

# Computes the largest integer k
def largest_k(N):
    iterator = 0
    sum = 0
    while ((sum + iterator) <= N):
        sum += iterator
        iterator += 2
    iterator -= 2
    return iterator


# Reads input
N = int(input('Enter a positive integer: '))

# Calls func largest_k
k = largest_k(N)

# Prints result
print(f'{k} is the largest k such that 0+2+4+6+...+k < {N}')
