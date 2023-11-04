# functions_for_lists.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022
from random import randint


def random_num_list(n):  # Generates a list of n integers
    return [randint(0, 100) for _ in range(n)]

# Takes a list as input and returns a list with only the odd values


def only_odd(lst):
    for i, num in enumerate(lst):
        if num % 2 == 0:
            lst.pop(i)
    return lst

# Takes a list as input and creates a new list with all the values squared


def square(lst):
    for i, num in enumerate(lst):
        lst[i] = num ** 2
    print(f'Let\'s square each number: {lst}')


# Returns a new list with only the values between start and stop in the list
def sublist(lst, start, stop):
    new_lst = []
    for i in range(start, stop):
        new_lst.append(lst[i])
    return new_lst


lst = random_num_list(10)
print(f'Here is the list: {lst}')
print(f'Odds in it are: {only_odd(lst)}')
square(lst)
print(f'Only the three middle values: {sublist(lst, 1,4)}')
