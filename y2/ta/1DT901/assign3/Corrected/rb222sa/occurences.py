from random import randint
lst = []
dct = {}

for i in range(100):
    num = randint(1, 10)
    lst.append(num)


def count_occurences(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    return dct


dct = count_occurences(lst)

for k, v in sorted(dct.items()):
    print(f"{k}\t{v}")
