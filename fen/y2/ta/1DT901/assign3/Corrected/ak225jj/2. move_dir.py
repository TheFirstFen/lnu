import os


def list_dir(dir_path):
    directories = []
    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    return directories


def ch_dir(dir_path):
    new_path = os.path.abspath(input(""))
    os.chdir(new_path)


def lst_files(dir_path):
    lst = []
    current_dir = os.scandir(dir.path)
    for entry in current_dir:
        if entry.is_file:
            lst.append(entry.name)
    return lst


use_input = 5
while use_input != 4:
    print("1. List directories ")
    print("2. Change directory ")
    print("3. List files ")
    print("4. Quit ")

    use_input = int(input("==> "))

    if use_input == 1:
        lst = list_dir(os.getcwd())
        for i in lst:
            print(i)
    if use_input == 2:
        ask = input("Name of directory to enter: ")
        os.chdir(ask)
    if use_input == 3:
        lst = lst_files(os.getcwd)
        for i in lst:
            print(i)
