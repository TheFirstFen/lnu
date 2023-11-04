import random


# my little function
def different(lst):
    list_set = set(lst)
    new_lst = list(list_set)
    return new_lst



# here starts the program
lst = []
for i in range(100):
    rand = random.randint(1, 200)
    lst.append(rand)

print(different(lst))
