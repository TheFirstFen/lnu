import random as r


# A Fuction to sort and count the ocurrences of a certain number
def count_occurrences(lst):
    for i in range(1, 11):
        rep = 0
        for j in range(len(lst)):
            if i == lst[j]:
                rep += 1
        lst2[i-1] = rep
    lst = list(set(lst))
    lst.sort()
    return lst, lst2


# What is needed to make the lists
lst = []
lst2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 100):
    lst.append(r.randint(1, 10))


# Receiving results from the function and displaying them
lst, lst2 = count_occurrences(lst)
for i in range(len(lst)):
    print(lst[i], lst2[i])
