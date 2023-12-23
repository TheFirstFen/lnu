import os


def mean(lst):
    return round(sum(lst) / len(lst), 1)


def std(lst):
    mean = sum(lst) / len(lst)
    variance = sum((x - mean)**2 for x in lst) / len(lst)
    stdev = variance ** 0.5
    return round(stdev, 1)


pathA = os.getcwd() + "/data/file_10k_integers_A.txt"
lstA = []
pathB = os.getcwd() + "/data/file_10k_integers_B.txt"
lstB = []


with open(pathA, "r") as file:
    for line in file:
        for i in line.split(","):
            lstA.append(float(i))

with open(pathB, "r") as file:
    for line in file:
        for i in line.split(":"):
            lstB.append(float(i))

print("Results for file A:")
print(f"Mean = {mean(lstA)}, Standard deviation = {std(lstA)} \n")
print("Results for file B:")
print(f"Mean = {mean(lstB)}, Standard deviation = {std(lstB)}")
