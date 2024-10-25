import random as rn


# Function for sorted dictionary
def count_occurrences(lst):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    for k, v in sorted(dct.items()):
        print(f"{k}\t{v}")


# Main program
lst = []
for i in range(1, 101):
    r = rn.randint(1, 10)
    lst.append(r)
count_occurrences(lst)
