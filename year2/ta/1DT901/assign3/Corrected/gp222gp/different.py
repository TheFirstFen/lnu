import random


def randomX200(x):
    randomlist = []
    for i in range(1, x+1):
        randomizer = random.randint(1, 200)
        randomlist.append(randomizer)
    return randomlist


def different(lst):
    uniques = set(lst)
    uniquelist = list(uniques)
    sortedlist = sorted(uniquelist)
    return sortedlist


print(different(randomX200(100)))
