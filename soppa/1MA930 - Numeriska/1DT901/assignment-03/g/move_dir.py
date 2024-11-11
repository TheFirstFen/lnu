import os


# Help function that prints elements in list provided
def print_list(lst):
    for str in lst:
        print(str)


# Returns true if entry is hidden
def is_hidden(entry):
    return entry.name.startswith(".")


# Returns a list of each directory
def list_dir(dir_path):
    dirs = []
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir() and not is_hidden(entry):
            dirs.append(entry.name)
    return dirs


# Returns a list of each file
def list_files(dir_path):
    files = []
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_file() and not is_hidden(entry):
            files.append(entry.name)
    return files


def change_path(input):
    return os.chdir(input)


path = os.getcwd()
ans = 0

# While loop that gets a new user input until 4 is entered
while ans != 4:
    ans = int(input("==> "))
    if ans == 1:
        dirs = list_dir(path)
        print_list(dirs)
    elif ans == 2:
        ninput = input("Name of directory to enter: ")
        path = change_path(ninput)
    elif ans == 3:
        fils = list_files(path)
        print_list(fils)
