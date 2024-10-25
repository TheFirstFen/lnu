import os


def mean(lst):
    return sum(lst) / len(lst)


def std(lst):
    avg = mean(lst)
    vri = sum([(xy - avg) ** 2 for xy in lst]) / (len(lst) - 1)
    return vri ** 0.5


def read(filename, delimiter):
    with open(filename, "r") as file:
        all_data = file.read().strip()
    all_data = all_data.replace("\n", delimiter)
    numbers = list(map(int, all_data.split(delimiter)))
    avg = mean(numbers)
    std_dev = std(numbers)
    print(f"resluts for {filename}:")
    print(f"mean = {avg:.1f}, standarad deviation = {std_dev:.1f}\n")


path = os.getcwd()
read(path + "/data/file_10k_integers_A.txt", ",")
read(path + "/data/file_10k_integers_B.txt", ":")
