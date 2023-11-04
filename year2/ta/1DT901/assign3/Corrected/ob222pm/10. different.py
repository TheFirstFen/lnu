import random


def different(lst):
    st = set(lst)
    new_lst = list(st)
    return new_lst


# program starts
lst = [random.randrange(1, 200) for i in range(100)]
print(different(lst))
