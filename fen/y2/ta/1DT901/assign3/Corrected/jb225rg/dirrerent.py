import random


# put integers into a set then back into list
def different(lst):
    diff = set()  # create set
    d_list = []  # create list
    for i in lst:
        diff.add(i)  # add ints to set
    for j in diff:
        d_list.append(j)  # att ints from set to list
    d_list.sort()  # sort the list
    return d_list


# main program
# create list of 200 integers in range 1,100
lst = [random.randint(1, 200) for n in range(0, 100)]
print(different(lst))
