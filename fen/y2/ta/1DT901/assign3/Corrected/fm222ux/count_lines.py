# Import Os module
import os

# Global variable/list for functions
file_list = []


# Function that returns list of file paths
def files(dir_path):
    entries = os.scandir(dir_path)
    for item in entries:
        if item.is_file() and item.name.endswith(".py"):
            file_list.append(item.path)
        if item.is_dir():
            files(item)
    return file_list


# Function that returns amount of lines from file path
def count_py_lines(dir_path):
    file_path_list = files(dir_path)

    counter = 0

    for file in file_path_list:
        lst = []
        newlst = []
        with open(file, "r") as r:
            for line in r:
                lst.append(line.strip())
            for item in lst:
                if item == "" or str(item).startswith("#"):
                    pass
                else:
                    newlst.append(item)
        counter += len(newlst)
    return counter


# Start of program

# Get path
path = os.getcwd()

# Result
print(f"The total amount of coded lines in {path} is {count_py_lines(path)}")
