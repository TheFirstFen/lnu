import os


def list_directories():

    path = os.getcwd()
    directories = []

    # go through the current directory and add directories to list
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(str(entry.name))

    # retuen list of found directories
    return directories


def change_directory(movement):
    path = os.getcwd()

    # enter new directory
    if movement == "..":
        os.chdir("../")
    else:
        os.chdir(path + "/" + movement)


def list_files():

    path = os.getcwd()
    files = []

    # find files and add name to list
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(str(entry.name))

    # retuen list of found files
    return files


def print_menu():
    print("1. List directories\n2. Change directory\n" +
          "3. List files\n4. Quit\n\n")


# main program starts
choise = True

while choise:

    print_menu()

    ans = int(input("==> "))

    # list directories
    if ans == 1:
        dirs = list_directories()
        for i in dirs:
            print(i)
        print()

    # change directory
    elif ans == 2:
        movement = input("Name of directory to enter: ")
        change_directory(movement)
        print()

    # list files
    elif ans == 3:
        files = list_files()
        for i in files:
            print(i)
        print()

    # quit
    else:
        choise = False
