import random


# Creating a def for sorting the list with sets.
# Creating a empty set and calling it s.
# For a value in the list add that value to the set.
# Make the set a list and return that list.
def different(lst):
    s = set()
    for n in lst:
        s.add(n)
    lst = list(s)
    lst.sort()
    return lst


# Empty list
lst = []
# Putting 100 random numbers in the list between the value 1 to 200.
for i in range(0, 100):
    a = random.randint(1, 200)
    lst.append(a)

# Printing the soorted list
print(different(lst))
