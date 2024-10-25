# Function to read numbers, then calculate mean and standard deviation.
# The 2 files imported, A and B. Have their structures of how numbers
# are listed differently therefor i check which file is currently
# being worked on by checking if the name of the file contains "A".
def read_file(path):
    lst = []
    with open(path, "r") as file:
        for num in file:
            if "A" in path:
                val = num.strip().split(",")
            else:
                val = num.strip().split(":")
            for value in val:
                try:
                    number = int(value)
                    lst.append(number)
                except ValueError:
                    pass
    return lst


# Function to calculate the mean.
def mean(lst):
    return round(sum(lst) / len(lst), 1)


# Function to calculate the mean.
def std(lst):
    avg = mean(lst)
    diff = [(x - avg) ** 2 for x in lst]
    mean_diff = mean(diff)
    return round(mean_diff**(1/2), 1)


"""
Main
"""
pathA = "data/file_10k_integers_A.txt"
pathB = "data/file_10k_integers_B.txt"

listA = read_file(pathA)
listB = read_file(pathB)

print(f"Results for file A:\nmean = {mean(listA)}, standard deviation" +
      f" = {std(listA)}")

print(f"Results for file B:\nmean = {mean(listB)}, standard deviation" +
      f"= {std(listB)}")
