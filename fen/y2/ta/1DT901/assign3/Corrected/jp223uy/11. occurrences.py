import random as rnd


def count_ocorruences(lst):
    count = {}  # Tuple
    for k in range(1, 11):
        count[k] = 0  # First place
    for i in lst:
        if i not in count:  # If not in dictionary
            count[i] = 0  # if not add the number
        count[i] += 1  # If in dictionary, append count

    for k, v in count.items():
        print(f"{k}\t{v}")  # Make space between columns


# Start program
lst = []
for i in range(100):
    lst.append(rnd.randint(1, 10))  # append the random dictionary

count_ocorruences(lst)  # No need to print, already in function
