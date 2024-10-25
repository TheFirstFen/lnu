import random


# counts occurances in dictionary
def count_occurances(lst):
    occ = {}  # empty dictionary
    for i in range(1, 11):  # create now, won't have to sort later
        occ[i] = 0
    for j in lst:
        occ[j] += 1  # add 1 for occurance
    return occ  # return dictionary


# main program
# generate list of 10 integers in range 1-100
lst = [random.randint(1, 10) for n in range(1, 101)]
occurances = count_occurances(lst)
# print the results
for k, v in occurances.items():
    print(f"{k:2}: {v}")
