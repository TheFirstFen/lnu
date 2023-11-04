import os


def read_file(file_path):
    lst = []
    with open(file_path, "r") as file:
        lst = file.readlines()
        return lst


def write_file(lines, file_path):
    with open(file_path, "w") as output_file:
        output_file.writelines(lines)


path = os.getcwd() + "/data/mamma_mia.txt"
lst = read_file(path)

print(f"\n Read{len(lst)} lines from file {path}")

path = os.getcwd() + "/data/output.txt"
write_file(lst, path)
print("Text saved in file", path)
