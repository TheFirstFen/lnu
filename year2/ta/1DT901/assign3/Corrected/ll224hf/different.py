import random


# Function to take in a list then return it sorted with no duplicates.
def different(lst):
    set_list = set()
    set_list.update(lst)
    return sorted(set_list)


"""
Main
"""
random_list = []
for i in range(100):
    r = random.randint(1, 200)
    random_list.append(r)

unique_list = different(random_list)
print(unique_list)
