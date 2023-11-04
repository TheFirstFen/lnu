import random as rn


# Sorting function
def different(lst):
    st = set(lst)
    new_lst = list(st)
    new_lst.sort()
    return new_lst


# Program starts
lst = []
for i in range(1, 101):
    r = rn.randint(1, 200)
    lst.append(r)
print(different(lst))
