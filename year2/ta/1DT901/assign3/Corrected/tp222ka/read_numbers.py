import os


def mean(lst):
    # sum of all interger / amount of integer
    sum = 0
    count_num = 0
    for num in lst:
        sum += num
        count_num += 1
    return sum / count_num


def std(lst):
    # Calculate mean by call the mean()
    mean_val = mean(lst)

    # Squared difference
    sqrt_dif = 0
    for i in lst:
        sqrt_dif += (i - mean_val)**2

    # Calculate the mean of the squared differences
    # To work out the mean, add up all the values then divide by how many
    sqrt_mean = sqrt_dif / len(lst)
    # Standard Deviation, take the square root of that
    std_dev = sqrt_mean ** 0.5
    return std_dev


def read_file(file_path):
    lst = []
    with open(file_path, "r") as file:
        for line in file:
            # Strip the line and replace : with , and split with ,
            number = line.strip().replace(":", ",").split(",")
            for num in number:
                lst.append(int(num))
                # anding num
    mean_value = mean(lst)
    std_value = std(lst)
    return mean_value, std_value


test_file = os.getcwd() + "/data/file_10k_integers_A.txt"
mean_value, std_value = read_file(test_file)
print("Results for file A: ")
print(f"mean = {mean_value:.1f}, standard deviation = {std_value:.1f}")


test_file_B = os.getcwd() + "/data/file_10k_integers_B.txt"
mean_value, std_value = read_file(test_file_B)
print("Results for file B: ")
print(f"mean = {mean_value:.1f}, standard deviation = {std_value:.1f}")
