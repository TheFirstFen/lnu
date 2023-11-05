import random


def random1to10(x):
    randomlist = []
    for i in range(1, x+2):
        randomizer = random.randint(1, 10)
        randomlist.append(randomizer)
    return randomlist


def count_occurences(lst):
    occurencedic = {
        "1's": 0,
        "2's": 0,
        "3's": 0,
        "4's": 0,
        "5's": 0,
        "6's": 0,
        "7's": 0,
        "8's": 0,
        "9's": 0,
        "10's": 0,
    }
    for numbers in range(1, 11):
        for checklst in range(1, len(lst)):
            if lst[checklst] == numbers:
                occurencedic[f"{numbers}'s"] += 1
    formatteddic = "\n".join([
        f"{key}: {value}" for key, value in occurencedic.items()])
    return formatteddic


print(count_occurences(random1to10(100)))
