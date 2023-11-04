# occurrences.py
#
# Author: Samuel Berg
# Date: 02-Oct-2022

from random import randint

'''count_occurrences(lst):
Creates a dict with the values of 1 - 10
each having the starting value of 0 to then
be incremented each time that specific value is
in given list and then returning the dictionary
when every element in given list has been checked.
'''


def count_occurrences(lst):
    my_dict = {
        '1': 0, '2': 0, '3': 0,
        '4': 0, '5': 0, '6': 0,
        '7': 0, '8': 0, '9': 0,
        '10': 0
    }

    for i in range(len(lst)):
        if lst[i] == 1:
            my_dict['1'] += 1
        elif lst[i] == 2:
            my_dict['2'] += 1
        elif lst[i] == 3:
            my_dict['3'] += 1
        elif lst[i] == 4:
            my_dict['4'] += 1
        elif lst[i] == 5:
            my_dict['5'] += 1
        elif lst[i] == 6:
            my_dict['6'] += 1
        elif lst[i] == 7:
            my_dict['7'] += 1
        elif lst[i] == 8:
            my_dict['8'] += 1
        elif lst[i] == 9:
            my_dict['9'] += 1
        elif lst[i] == 10:
            my_dict['10'] += 1
    return my_dict


# Main code
lst = list(randint(0, 10) for i in range(0, 100))
my_dict = count_occurrences(lst)
for i in range(1, 11):
    print(f'{str(i)}\t{my_dict[str(i)]}')
