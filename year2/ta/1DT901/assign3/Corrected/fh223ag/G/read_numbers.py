import os

# we will need two lists to store the integers and the paths to the txt files
lst_i_first = []
lst_i_second = []
full_text = ""
index = 0
first_path = os.getcwd() + "/data/file_10k_integers_A.txt"
second_path = os.getcwd() + "/data/file_10k_integers_B.txt"


# Function used to read and format first file
def read_first(dir_path):
    with open(dir_path, "r") as file:
        global index
        as_string = file.read()
        as_string = as_string.replace(", ", " ")
        string_list = as_string.split()
        for i in string_list:
            n = string_list[index].replace(",", "")
            lst_i_first.append(int(n))
            index += 1
        return lst_i_first


# Function used to read and format second file
def read_second(dir_path):
    with open(dir_path, "r") as file:
        as_string = file.read()
        as_string = as_string.replace(":", " ")
        string_list = as_string.split()
        for i in string_list:
            lst_i_second.append(int(i))
    return lst_i_second


# Function to calculate mean of any list
def mean(lst):
    sum = 0
    mean = 0
    for i in lst:
        sum += i
    mean = sum / len(lst)
    return round(mean, 1)


# Function to calculate standard deviation of any list
def std(lst):
    std_sum = 0
    std_mean = 0
    std_end = 0
    square_lst = []
    mean_of_lst = mean(lst)
    for i in lst:
        square_lst.append((i - mean_of_lst) ** 2)
        std_sum += (i - mean_of_lst) ** 2
    std_mean = std_sum / len(square_lst)
    std_end = std_mean ** (1/2)
    return round(std_end, 1)


# Calculations
read_first(first_path)  # Initilize first file
read_second(second_path)  # Initilize second file
average_first = mean(lst_i_first)  # Mean of the first file
std_first = std(lst_i_first)  # std of the first file
average_second = mean(lst_i_second)  # Mean of the second list
std_second = std(lst_i_second)  # Std of the second list

# Print results
print("Results for file A:")
print(f"mean = {average_first}, standard deviation = {std_first}")
print("\nResults for file B")
print(f"mean = {average_second}, standard deviation = {std_second}")
