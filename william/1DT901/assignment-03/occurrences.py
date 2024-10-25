import random


def count_occurrences(lst):
    # creates a sorted dict from 1 - 11
    occurrences = {num: 0 for num in range(1, 11)}

    for num in lst:
        occurrences[num] += 1

    for num, count in occurrences.items():
        print(num, "\t", count)


lst = [random.randint(1, 10) for i in range(100)]
count_occurrences(lst)
