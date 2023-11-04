import random

lst_ints = [random.randint(1, 10) for i in range(100)]  # Random list


def count_occurences(lst):
    dct = {}  # Empty dictionary
    for z in range(1, 11):   # Add keys 1-10
        dct[z] = 0
    for i in lst:  # count occurences
        dct[i] += 1
    for k, v in dct.items():  # Print results
        print(k, v)
    return dct


count_occurences(lst_ints)  # Initizalise
