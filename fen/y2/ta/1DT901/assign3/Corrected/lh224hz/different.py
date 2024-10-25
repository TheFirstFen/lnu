import random


def different(lst):
    sorted_set_lst = sorted(set(lst))
    return sorted_set_lst


lst = []
while len(lst) <= 100:
    n = random.randint(1, 200)
    if n not in lst:
        lst.append(n)


print("Different integers: ", different(lst))
