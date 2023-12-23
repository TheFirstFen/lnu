import math
import os


def mean(lst):
    # computes the avreage  of list
    return sum(lst) / len(lst)


def std(lst):  # this definition computes the standard deviation of numbers list
    number = len(lst)
    me_an = mean(lst)
    compute = sum((x - me_an) ** 2 for x in lst) / number
    s_ = math.sqrt(compute)
    return s_


# read file and cuts the lines and convert numbers
def read_file(fi_le, specif):
    infor_lst = []
    fi_le = os.getcwd() + fi_le
    with open(fi_le, "r") as file:
        for numb_line in file:
            for num in numb_line.strip().split(specif):
                # after all operation will collects all in infor_lst
                infor_lst.append(int(num))
    return infor_lst


information_f_A = read_file("/data/file_10k_integers_A.txt", ",")
information_f_B = read_file("/data/file_10k_integers_B.txt", ":")


print("Resultat for file A: ")
print("mean = ", round(mean(information_f_A), 1),
      'standdard deviation =', round(std(information_f_A), 1))
print()
print("Resultat for file B: ")
print("mean = ", round(mean(information_f_B), 1),
      'standard deviation = ', round(std(information_f_B), 1))
