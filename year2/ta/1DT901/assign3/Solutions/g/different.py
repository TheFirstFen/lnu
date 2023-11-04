import random


def different(lst):
    theSet = set()

    for n in lst:
        theSet.add(n)

    new_list = list(theSet)
    new_list.sort()

    return new_list


# Main program
num_lst = [random.randint(1, 200) for i in range(100)]

diff = different(num_lst)
print('Different integers:')
print(diff)
