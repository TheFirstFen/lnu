import os


# Help function that returns how many non empty lines are in file
def check_lines(entry):
    temp_num = 0
    with open(entry, "r") as file:
        for lines in file:
            if lines != "\n":
                temp_num += 1
    return temp_num


# Goes through each directory to count lines of code written
def count_py_lines(dir_path):
    global num
    entries = os.scandir(dir_path)
    for entry in entries:
        # Checks if entry is a directory
        if entry.is_dir():
            n_entry = os.chdir(entry)
            count_py_lines(n_entry)
            n_entry = os.chdir("..")
        # if entry is a python file counts amount of lines and adds to total
        elif entry.name.endswith(".py"):
            num += check_lines(entry)
    return num


num = 0

path = os.getcwd()
num = count_py_lines(path)
print(num)
