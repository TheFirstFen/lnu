import math
import os


# Creating a def called mean with a variable set to zero.
# for i in a list add value from i to sum. divide sum by the lenght 
# of the list to get the mean and return mean.
def mean(lst):
    sum = 0
    for i in lst:
        sum += i
    mean = round(sum/len(lst), 1)
    return mean


# Creat a def called std with to variables, one set to zero and on set
# to an empty list. for every value in a list divide by the mean and square it
# Append to the new list and add that value to the variable named sum.
# take the square root of the sum divided by the lenght of the list and return.
def std(lst):
    sum = 0
    sq_val_lst = []
    for i in lst:
        res = (i - mean(lst)) ** 2
        sq_val_lst.append(res)
    for i in sq_val_lst:
        sum += i
    std = round(math.sqrt(sum/(len(lst))), 1)
    return std


# Creating a def called opening_a, which opens the a file and splits the values
# in to a list called lst.
def opening_a(path):
    lst = []
    with open('file_10k_integers_A.txt', "r") as file:
        file_row = file.read()
        file_lst = file_row.split(", ")
        for i in file_lst:
            if "\n" in i:
                temp_lst = i.split("\n")
                lst.append(int(temp_lst[0]))
                if temp_lst[1] != "":
                    lst.append(int(temp_lst[1]))
            else:
                lst.append(int(i))
    return lst


# does the same as opening_a but for file b.
def opening_b(path):
    lst = []
    with open('file_10k_integers_B.txt', "r") as file:
        file_row = file.read()
        file_lst = file_row.split(":")
        for i in file_lst:
            if "\n" in i:
                temp_lst = i.split("\n")
                lst.append(int(temp_lst[0]))
                if temp_lst[1] != "":
                    lst.append(int(temp_lst[1]))
            else:
                lst.append(int(i))
    return lst


# goes in to the mapp_10k_integers.
path = os.chdir("mapp_10k_integers")
# calling the functions and naming them to a easier name.
lst = opening_a(path)
lst_b = opening_b(path)

# printing the mean and std for both files.
print(f"mean: {mean(lst)}, standard diviation:  {std(lst)}")
print(f"mean: {mean(lst_b)}, standard diviation: {std(lst_b)}")
