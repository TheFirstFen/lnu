import random


def different(lst):  # If the integers already found, remove
    st = set(lst)  # New lst
    list_new = list(st)  # Antoher new from the old
    return list_new


# Start program
lst = {random.randint(1, 200) for i in range(100)}  # 100 int between 1-200
print("Different integers:")
print(different(lst))
