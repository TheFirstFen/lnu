import random


def count_occurrences(lst):
    dct = {}

    for n in lst:
        if n not in dct:
            dct[n] = 0
        dct[n] += 1

    dct = sorted(dct.items(), key=lambda tpl: tpl[0])

    return dct


# Main program
num_lst = [random.randint(1, 10) for i in range(100)]

occurs = count_occurrences(num_lst)

for i in range(len(occurs)):
    print(f'{occurs[i][0]}\t{occurs[i][1]}')
