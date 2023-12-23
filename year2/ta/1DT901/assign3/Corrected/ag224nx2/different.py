import random


def different(lst):
    settet = set(lst)
    unika = list(settet)

    return unika


# program starts
listan_random = []

for i in range(0, 100):
    rd = random.randint(1, 200)
    listan_random.append(rd)

sorted_list = different(listan_random)
print(sorted_list)
