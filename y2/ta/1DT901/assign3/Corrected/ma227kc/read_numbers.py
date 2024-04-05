import os


# importing documents and assigning variables
path = os.getcwd()
docA = path + "/data/file_10k_integers_A.txt"
docB = path + "/data/file_10k_integers_B.txt"
fileA = open(docA)
fileB = open(docB)


# A function that calculates the mean for both docs
def mean(lst):
    sum = 0
    lst = []

    for line in fileA:
        lst += line.split(",")
    for item in lst:
        sum += int(item)
    meanA = round(sum / len(lst), 1)

    sum = 0
    lst = []
    for line in fileB:
        lst += line.split(":")
    for item in lst:
        sum += int(item)
    meanB = round(sum / len(lst), 1)

    return meanA, meanB


# The means which are needed to calculate the standard deviation
meanA, meanB = mean("")


# Didn't work without those two here.
# I would assume the ones above were not public
# and only accessable to mean(lst)
fileA = open(docA)
fileB = open(docB)


# Calculates the standard deviation
def std(lst):
    devA = 0
    devB = 0
    lst = []

    for line in fileA:
        lst += line.split(",")
    for item in lst:
        devA += (int(item)-meanA)**2
    devA = round((devA/len(lst))**0.5, 1)

    lst = []
    for line in fileB:
        lst += line.split(":")
    for item in lst:
        devB += (int(item)-meanB)**2
    devB = round((devB/len(lst))**0.5, 1)

    return devA, devB


# I need those variable for the display
devA, devB = std("")


# Displaying. Two prints are better than one that is too long
# because of Flake8
print(f"The mean and standard deviation for file A:\nmean: {meanA}"
      + f"   standard deviation: {devA}")

print(f"The mean and standard deviation for file B:\nmean: {meanB}"
      + f"   standard deviation: {devB}")
