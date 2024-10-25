import os


def read_file(file_path):
    lst = []
    with open(file_path, "r") as file:
        lst = file.readlines()
        return lst


def write_file(lst, file_path):
    with open(file_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(lst)


# program starts
path = os.getcwd() + "/data/mamma_mia.txt"
lst = read_file(path)

# read text file
print(f"\nRead {len(lst)} lines from file {path}")

# write text file
path = os.getcwd() + "/data/output.txt"
write_file(lst, path)
print("Text saved in file", path)
print()
