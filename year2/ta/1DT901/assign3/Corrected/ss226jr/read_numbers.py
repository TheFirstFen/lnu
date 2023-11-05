import math
import os

home = os.getcwd()
a = "file_10k_integers_A.txt"
b = "file_10k_integers_B.txt"


def read(path, file):
    path += "/" + file
    fle = open(path, "r")
    lts = []
    if file == 'file_10k_integers_B.txt':
        for i in fle:
            nn = i.split(":")
            for numbers in nn:
                lts.append(numbers)
    else:
        for i in fle:
            nn = i.rstrip("\n")
            nn = nn.split(",")
            for numbers in nn:
                lts.append(numbers)
    fle.close()
    return lts


def mean(lst):
    sm = 0
    for i in lst:
        i = int(i)
        sm += i
        mn = round(sm / len(lst), 1)
    return mn


def std(lst, m):
    dv = 0
    for i in lst:
        cc = 0
        i = int(i)
        cc = (i - m) ** 2
        dv += cc
        stds = round(math.sqrt(dv / len(lst)), 1)
    return stds


A_1 = read(home, a)
m_1 = mean(A_1)
std_1 = std(A_1, m_1)
print("Results for file A:")
print(f"Mean: {m_1}, standarde deviation = {std_1}")

A_2 = read(home, b)
m_2 = mean(A_2)
std_2 = std(A_2, m_2)
print("Results for file B:")
print(f"Mean: {m_2}, standarde deviation = {std_2}")
