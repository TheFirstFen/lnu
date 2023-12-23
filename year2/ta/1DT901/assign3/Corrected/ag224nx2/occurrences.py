import random as rnd


def count_occurrences(lst):
    set_list = set(lst)
    sorted_list = sorted(set_list)

    dct_count = {}
    count = 0
    for j in range(0, len(sorted_list)):
        for k in range(0, len(lst)):
            if sorted_list[j] == lst[k]:
                count += 1
        dct_count[sorted_list[j]] = count
        count = 0

    for k, v in dct_count.items():
        print(f'{k}   {v} \n')


# program starts
listan_random = []

for i in range(0, 100):
    rd = rnd.randint(1, 10)
    listan_random.append(rd)

count_occurrences(listan_random)
