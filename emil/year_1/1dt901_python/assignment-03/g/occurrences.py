import random


# creating a def called count_occurrences that containes some variables 
# set to zero and a dictionary with the key set from 1 to 10
# The variables then get set to the value. If a number in the 
# list is one of the keys the corresponding variable gets one added to it.
# Returning the dictionary with modified variables
def count_occurrences(lst):
    a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    dct = {1: a, 2: b, 3: c, 4: d, 5: e, 6: f, 7: g, 8: h, 9: i, 10: j}
    for i in lst:
        if i == 1:
            a += 1
            dct[1] = a
        if i == 2:
            b += 1
            dct[2] = b
        if i == 3:
            c += 1
            dct[3] = c
        if i == 4:
            d += 1
            dct[4] = d
        if i == 5:
            e += 1
            dct[5] = e
        if i == 6:
            f += 1
            dct[6] = f
        if i == 7:
            g += 1
            dct[7] = h
        if i == 8:
            h += 1
            dct[8] = h
        if i == 9:
            i += 1
            dct[9] = i
        if i == 10:
            j += 1
            dct[10] = j
    return dct


# Creating a random list with 100 numbers from 1 to 10
lst = []
for i in range(0, 100):
    a = random.randint(1, 10)
    lst.append(a)

# Printing the key and value from the dictionary.
for key, value in count_occurrences(lst).items():
    print(key, "   ", value)
