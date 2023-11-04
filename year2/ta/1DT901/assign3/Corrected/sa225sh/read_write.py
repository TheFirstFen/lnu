import os


def read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            file_content = file.read()
            line = file_content.split("\n")
            return line


def write_file(lines, file_path):
    if os.path.isfile(file_path):
        with open(file_path, "a") as file:
            for line in lines:
                file.write(line + "\n")
            return "Done"


path = os.getcwd() + "/Sa225sh_assign3/input/mamma_mia.txt"
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")
path_2 = os.getcwd() + "/Sa225sh_assign3/output/output.txt"
write_file(lst, path_2)
print("Text saved in file", path_2)
