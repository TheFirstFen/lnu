# Import os module
import os


# Function for calculating average
def mean(lst):
    sum = 0
    for item in lst:
        sum += int(item)

    average = sum / len(lst)
    return round(average, 1)


# Function for calculating standard deviation
def std(lst, mean):
    e = [(int(num) - mean)**2 for num in lst]
    sum = 0
    for item in e:
        sum += int(item)

    average = sum / len(lst)
    return round((average)**0.5, 1)


# Get path
path = os.getcwd()

pathA = path + "/data/file_10k_integers_A.txt"

pathB = path + "/data/file_10k_integers_B.txt"

# Split files into lists
with open(pathA, "r") as a:
    lstA = a.read().strip().replace("\n", " ").replace(",", " ").split()

with open(pathB, "r") as b:
    lstB = b.read().split(":")

# Result
print("Result for file A: ")
print(f"mean = {mean(lstA)}, standard deviation = {std(lstA,mean(lstA))}\n")

print("Result for file B: ")
print(f"mean = {mean(lstB)}, standard deviation = {std(lstB,mean(lstB))}")
