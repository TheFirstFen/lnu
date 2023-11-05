import os


def read_integers(path):
    lst = []
    with open(path, "r") as infile:
        lines = infile.readlines()
        for line in lines:
            if ":" in line:
                substrings = line.split(":")
                for substring in substrings:
                    n = int(substring.strip())
                    lst.append(n)
            else:
                numbers = line.split(",")
                for number in numbers:
                    n = int(number.strip())
                    lst.append(n)
    return std(lst), mean(lst)


def mean(lst):
    return sum(lst) / len(lst)


def std(lst):
    avg = mean(lst)
    variance = sum((x - avg) ** 2 for x in lst) / len(lst)
    return variance ** 0.5


pathA = os.getcwd() + "/data/inta.txt"
pathB = os.getcwd() + "/data/intb.txt"

A = read_integers(pathA)
B = read_integers(pathB)
print("Results for file A: ")
print("Mean: =", round(A[1], 1), ", standard deviation: =", round(A[0], 1))
print()
print("Results for file B: ")
print("Mean: =", round(B[1], 1), ", standard deviation: =", round(B[0], 1))
