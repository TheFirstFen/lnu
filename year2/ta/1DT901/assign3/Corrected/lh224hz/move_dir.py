import os


def list_dir(dir_path):
    lst = []
    dirs = os.scandir(dir_path)

    for dir in dirs:
        if dir.is_dir():
            lst.append(dir.name)
    return lst


def change_dir(dir_path):
    new = os.path.abspath(dir_path)
    os.chdir(new)


def list_files(dir_path):
    lst = []
    files = os.scandir(dir_path)

    for file in files:
        if file.is_file():
            lst.append(file.name)
    return lst


# Program start
running = True

while running:
    dir_path = os.getcwd()
    print("1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    user_input = int(input("Select option: "))
    if user_input == 1:
        dirs = list_dir(dir_path)
        for dir in dirs:
            print(dir)
    if user_input == 2:
        new_path = input("Name of directory to enter: ")
        change_dir(new_path)
    if user_input == 3:
        files = list_files(dir_path)
        for file in files:
            print(file)
    if user_input == 4:
        running = False
