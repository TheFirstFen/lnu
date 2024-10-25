# salary_revision.py
#
# Author: Samuel Berg
# Date: 11-Sep-2022

def median(lst):
    mid = len(lst) // 2
    return (lst[mid] + lst[~mid]) / 2


# Creates a list to store the salaries in
salaries = []
# Takes a input of a long string with salaries split only
# with whitespaces
temp = input('Provide salaries: ')
# Puts all of the input into a list as separate salaries by splitting
# at whitespaces
salaries = temp.split(' ')
avg = 0

# Put all the give salaries into a list as integers
# and adds every salary in salaries together as variable avg
for i in range(len(salaries)):
    salaries[i] = int(salaries[i])
    avg += salaries[i]

# Computes the average salary of given salaries
avg /= len(salaries)
# Sorts the list of salaries from lowest to highest
salaries.sort()

'''
Computes the median salary of given salaries and prints it rounded off
also prints the rounded off average salary and lastly computes and prints
the gap between the minimum and maximum salaries
'''
print('Median: ', round(median(salaries)))
print('Average: ', round(avg))
print('Gap: ', (max(salaries) - min(salaries)))
