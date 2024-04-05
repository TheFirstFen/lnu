# read_numbers.py
#
# Author: Samuel Berg
# Date: 05-Oct-2022

from math import sqrt
import os

'''mean(lst):
Computes the mean value of the given lst.
'''


def mean(lst):
    tot_val = 0
    for i in lst:
        tot_val += i
    return round(tot_val / len(lst), 1)


'''std(lst):
Computes the standard deviation value of the given lst.
'''


def std(lst):
    temp_lst = []
    avg = mean(lst)
    for i in lst:
        temp = (i - avg) ** 2
        temp_lst.append(temp)
    return round(sqrt(mean(temp_lst)), 1)


'''open_file_a():
Opens specified file in specified path
and converts each line into a index in a
list which then it replaces all the "," and
new line characters with spaces. Then
it goes through each line and when it
finds the " " character it adds the
found numbers before that space in a
row to a list which is returned on
completion.
'''


def open_file_a():
    with open(file_a, 'r') as file:
        temp = file.readlines()
        lst = []
        num = ''
        for line in temp:
            line = line.replace(', ', ' ')
            line = line.replace('\n', ' ')
            for number in line:
                if ord(number) == 32:
                    lst.append(int(num))
                    num = ''
                else:
                    num += number
    return lst


'''open_file_b():
Opens specified file in specified path
and converts each line into a index in a
list. Then it goes through each line and when it
finds the ":" character it adds the
found numbers before that space in a
row to a list which is returned on
completion.
'''


def open_file_b():
    with open(file_b, 'r') as file:
        temp = file.readlines()
        lst = []
        num = ''
        for line in temp:
            for number in line + chr(58):
                if ord(number) == 58:
                    lst.append(int(num))
                    num = ''
                else:
                    num += number
    return lst


# Main code
path = os.getcwd()
path = path + ('/data/file_10k_integers/')

file_a = f'{path}file_10k_integers_A.txt'
file_b = f'{path}file_10k_integers_B.txt'

lst_a = open_file_a()
lst_b = open_file_b()

print('Results for file A:')
print(f'mean = {mean(lst_a)}, standard deviation = {std(lst_a)}')
print('\nResults for file B:')
print(f'mean = {mean(lst_b)}, standard deviation = {std(lst_b)}')
