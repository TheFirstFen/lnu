import random as r


# A function that receives a list then removes duplicates and sorts it.
def different(lst):
    lst = list(set(lst))
    lst.sort()
    return lst


# The list that will be given to the function
lst = []
# A loop to add a hundred random integers to the list
for i in range(0, 100):
    lst.append(r.randint(1, 200))


# Displaying results
print(different(lst))
