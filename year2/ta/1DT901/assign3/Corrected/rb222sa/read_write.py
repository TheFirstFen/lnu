import os

path = os.getcwd() + "/mamma_mia.txt"
output = os.getcwd() + "/output.txt"


def read_file(path):
    lst = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            lst.append(line)
    return lst


def write_file(lines, output):
    with open(output, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


lines = read_file(path)

write_file(lines, output)
