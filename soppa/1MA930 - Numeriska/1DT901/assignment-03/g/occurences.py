import random as rd


# Help function to sort the dictionary
def get_key(tpl):
    return tpl[0]


# Returns a sorted dictionary of numbers in list provided
def count_occurances(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    items = list(dct.items())
    sorted_key = sorted(items, key=get_key)
    return sorted_key


lst = []
# Creates a list of 100 random integers between 1 and 10
for n in range(100):
    n = rd.randint(1, 10)
    lst.append(n)

dct = count_occurances(lst)
for str in dct:
    print(f"{str[0]}\t{str[1]}")
