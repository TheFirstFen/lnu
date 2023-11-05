import random


def count_occurrences(lst):
    occurrences = {}
    for num in lst:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    return occurrences


random_list = []
for i in range(100):
    random_list.append(random.randint(1, 10))

dict = count_occurrences(random_list)

for i in range(1, 11):
    print(f"{i}\t{dict.get(i, 0)}")
