# different.py
#
# Author: Samuel Berg
# Date: 02-Oct-2022

from random import randint

'''different(lst):
Converts given list into a set by adding value
after value to a set and then converting that set
back into a list which is then sorted and returned.
'''


def different(lst):
    myset = set()
    for i in range(len(lst)):
        myset.add(lst[i])
    new_lst = list(myset)
    new_lst.sort()
    return new_lst


# Main code
lst = list(randint(0, 200) for i in range(0, 100))

print(f'Different integers:\n{different(lst)}')
