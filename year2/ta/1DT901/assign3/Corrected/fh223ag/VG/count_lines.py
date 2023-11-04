import os
path = "/Users/filiphelgesson/Desktop/Software/"\
    "Python project/introduction to programming (1DT901)/Labbar"
path_lst = []  # lst outside function so that it´s not resetting


def find_pyfiles(dir_path):  # Function used to find all .py files
    global path_lst
    entries = os.scandir(dir_path)
    for i in entries:
        if i.is_file() and i.name.endswith(".py"):
            path_lst.append(i.path)
        if i.is_dir():
            find_pyfiles(i.path)
    return path_lst


def count_py_lines(dir_path):  # find all lines without space in files
    lines_str = []  # Each line stored as a listobject
    for i in find_pyfiles(dir_path):  # Iterate the list of .py files
        with open(i, "r") as file:
            for line in file:
                if not line.isspace():  # Remove lines that are blank
                    lines_str.append(line.split("\n"))
    return len(lines_str)


# Main program
print(count_py_lines(path), "Lines of code")
