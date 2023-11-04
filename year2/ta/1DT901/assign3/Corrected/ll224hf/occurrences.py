import random


def count_occurrences(lst):
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in lst:
        count[i] += 1
    for k, v in count.items():
        print(f"{k}\t{v}")


"""
Main
"""

random_list = []
for i in range(100):
    random_list.append(random.randint(1, 10))

random_dict = count_occurrences(random_list)
