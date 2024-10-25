import random


def count_occurrences(lst):
    count = {}
    for k in range(1, 11):
        count[k] = 0
    for i in lst:
        if i not in count:
            count[i] = 0
        count[i] += 1

    for k, v in count.items():
        print(f"{k}\t{v}")


# main program starts
lst = []
for i in range(100):
    lst.append(random.randint(1, 10))

(count_occurrences(lst))
