import os
from math import sqrt

# Since I was the one generating the two data sets I know
# that set A should have a mean=250, std=70, and set B
# should have mean=10, std=100


# File A reading
def read_file_A(path):
    with open(path, "r") as file:
        lst = []
        for line in file:
            as_strings = line.split(", ")
            as_ints = [int(s) for s in as_strings]
            lst += as_ints
        return lst


# File B reading
def read_file_B(path):
    with open(path, "r") as file:
        line = file.readline()
        as_strings = line.split(":")
        as_ints = [int(s) for s in as_strings]
        return as_ints


def mean(lst):
    s = sum(lst)
    n = len(lst)
    return s/n


def std(lst):
    m = mean(lst)
    sq = [(x-m)**2 for x in lst]
    std = sqrt(sum(sq)/len(lst))
    return std


# Program starts
# Read File A
path = os.getcwd() + "/data/file_10k_integers_A.txt"
ints = read_file_A(path)

m = round(mean(ints), 1)
sd = round(std(ints), 1)
print(f"\nResults for {path}\nmean= {m}, std={sd}")

# File B
path = os.getcwd() + "/data/file_10k_integers_B.txt"
ints = read_file_B(path)

m = round(mean(ints), 1)
sd = round(std(ints), 1)
print(f"\nResults for {path}\nmean= {m}, std={sd}")
