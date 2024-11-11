import os


# Returns mean of given list
def mean(lst):
    n = 0
    for i in lst:
        n += i
    mean = n / len(lst)
    return mean


# Returns standrad deviation of given list
def std(lst):
    sum = 0
    for i in lst:
        n = i - mean(lst)
        num = n * n
        sum += num
    n_mean = sum / len(lst)
    std = n_mean ** 0.5
    return std


# Reads the file and returns a list of all integers
def read_file_a(path, name):
    i_lst = []
    with open(path + "/" + name, "r") as file:
        as_string = file.read()
        n_string = as_string.strip()
        ne_string = n_string.replace("\n", ", ")
        lst = ne_string.split(", ")
        # Appends each string as an integer to an empty list
        for s in lst:
            i_lst.append(int(s))
    return i_lst


# Reads the file and returns a list of all integers
def read_file_b(path, name):
    i_lst = []
    with open(path + "/" + name, "r") as file:
        as_string = file.read()
        lst = as_string.split(":")
        # Appends each string as an integer to an empty list
        for s in lst:
            i_lst.append(int(s))
    return i_lst


path = os.chdir("files2read")
path = os.getcwd()

# Prints the rounded and correct results
name_a = "file_10k_integers_A.txt"
lst_a = read_file_a(path, name_a)
mean_a = round(mean(lst_a), 1)
std_a = round(std(lst_a), 1)
print("Results for file A:")
print(f"Mean = {mean_a}, standard deviation = {std_a}")

name = "file_10k_integers_B.txt"
lst_b = read_file_b(path, name)
mean_b = round(mean(lst_b), 1)
std_b = round(std(lst_b), 1)
print("Results for file B:")
print(f"Mean = {mean_b}, standard deviation = {std_b}")
