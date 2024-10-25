import os
import math

fileApath = (os.getcwd() + "/file_10k_integers_A.txt")
fileBpath = (os.getcwd() + "/file_10k_integers_B.txt")


def mean(path):
    lst = []
    total = 0
    mean = 0
    with open(path, "r") as file:
        current = ""
        readfile = file.read()
        for number in readfile:
            if number.isdigit() or (number == "-" and not current):
                current += number
            else:
                if current:
                    lst.append(int(current))
                current = ""
        if current:
            lst.append(int(current))
    if lst:
        total = sum(lst)
    for itemid in range(0, len(lst)):
        total = total + lst[itemid]
    mean = total/(len(lst)*2)
    return mean


def std(path):
    lst = []
    total = 0
    mean2 = 0
    with open(path, "r") as file:
        current = ""
        readfile = file.read()
        for number in readfile:
            if number.isdigit() or (number == "-" and not current):
                current += number
            else:
                if current:
                    lst.append(int(current))
                current = ""
        if current:
            lst.append(int(current))
    if lst:
        total = sum(lst)
    for itemid in range(0, len(lst)):
        total = total + lst[itemid]
    mean2 = total / (len(lst) * 2)
    squared_diff = [(x - mean2) ** 2 for x in lst]
    var = sum(squared_diff) / len(lst)
    sdevi = math.sqrt(var)
    return sdevi


print("Results for file A:")
print("Mean:", str(mean(fileApath)) + ", Standard Deviation:", std(fileApath))
print("Results for file B:")
print("Mean:", str(mean(fileBpath)) + ", Standard Deviation:", std(fileBpath))
