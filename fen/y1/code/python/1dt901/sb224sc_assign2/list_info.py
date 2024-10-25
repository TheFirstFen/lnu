# list_info.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022
from random import randint
lst = [randint(1, 10000) for i in range(100)]
num = 0

print(f'Largest value in list: {max(lst)}')
print(f'Smallest value in list: {min(lst)}')

for i in lst:
    num += i
print(f'Average value in list: {round(num/len(lst), 2)}')

lst.sort()
print(f'Second largest value in list: {lst[-2]}')
