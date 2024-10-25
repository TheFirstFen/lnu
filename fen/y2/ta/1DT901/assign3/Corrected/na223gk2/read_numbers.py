import os


def mean(lst):
    total = 0
    count = 0
    for num in lst:
        total += num
        count += 1
    return total / count


def std(lst):
    avg = mean(lst)
    variance = sum((x - avg) ** 2 for x in lst) / len(lst)
    return variance ** 0.5


def read_file(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers


file1 = os.getcwd() + "/data/file_10k_integers_A.txt"
file2 = os.getcwd() + "/data/file_10k_integers_B.txt"

numbers1 = read_file(file1)
numbers2 = read_file(file2)

mean1 = mean(numbers1)
std1 = std(numbers1)
mean2 = mean(numbers2)
std2 = std(numbers2)

print(f"File: {file1}")
print(f"Mean: {mean1}")
print(f"Standard Deviation: {std1}")
print()
print(f"File: {file2}")
print(f"Mean: {mean2}")
print(f"Standard Deviation: {std2}")
