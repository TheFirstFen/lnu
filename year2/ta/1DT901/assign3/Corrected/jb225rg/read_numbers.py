import os


def mean(lst):
    summa = sum(lst)
    mean = summa/10000
    mean = round(mean, 1)
    return mean


def std(lst):
    summ = 0
    mean_ = mean(lst)
    for i in lst:
        m = i - mean_
        m2 = m*m
        summ += m2
    n = summ/10000
    std = n**(1/2)
    std = round(std, 1)
    return std


# main program starts
# file A
path = os.getcwd() + '/assignment3/file_10k_integers/file_10k_integers_A.txt'
lst_a = []

with open(path, 'r') as a_file:
    for row in a_file:

        # get numbers by themselves
        ints = row.strip()
        ints = ints.replace(" ", "")
        ints = ints.split(',')

        # add numbers to lsit
        for i in ints:
            lst_a.append(int(i))

# file B
path = os.getcwd() + '/assignment3/file_10k_integers/file_10k_integers_B.txt'
lst_b = []

with open(path, 'r') as b_file:
    for row in b_file:
        # seperate numbers
        ints_b = row.split(":")

        # add numbers to list
        for j in ints_b:
            lst_b.append(int(j))


# call functions
mean_a = mean(lst_a)
std_a = std(lst_a)
mean_b = mean(lst_b)
std_b = std(lst_b)

# print resaults
print("Resaults for file A:")
print(f"mean = {mean_a}, standard deviation = {std_a}")
print()
print("Resaults for file B:")
print(f"mean = {mean_b}, standard deviation = {std_b}")
