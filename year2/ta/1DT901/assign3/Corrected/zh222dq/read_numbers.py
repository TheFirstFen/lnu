import os


# Function for reading file A
def read_fileA(file_path):
    lst = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean = line.strip().split(", ")
            for c in clean:
                lst.append(int(c))
    return lst


# Function for reading file B
def read_fileB(file_path):
    lst = []
    with open(file_path, "r", encoding="utf-8") as file:
        full_text = file.read()
        clean = full_text.split(":")
        for c in clean:
            lst.append(int(c))
    return lst


# Function that calculates the mean
def the_mean(lst):
    len_lst = len(lst)
    sum_lst = 0
    for i in lst:
        sum_lst += i
    return round(sum_lst/len_lst, 1)


# Function that calculates the standard deviation
def std(lst):
    mean = the_mean(lst)
    len_lst = len(lst)
    standard_division = (sum(pow(x - mean, 2) for x in lst) / len_lst)**0.5
    return round(standard_division, 1)


# Program starts A
pathA = os.getcwd() + "/data/file_10k_integers_A.txt"

# Read text file A
lstA = read_fileA(pathA)

# Results for file A:
meanA = the_mean(lstA)
stdA = std(lstA)
print("Results for file A: ")
print(f"mean = {meanA}, standard deviation = {stdA}")


# Program starts B
pathB = os.getcwd() + "/data/file_10k_integers_B.txt"

# Read text file B
lstB = read_fileB(pathB)

# Results for file B
meanB = the_mean(lstB)
stdB = std(lstB)
print("Results for file B: ")
print(f"mean = {meanB}, standard deviation = {stdB}")
