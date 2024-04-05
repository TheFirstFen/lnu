import os


def list_dir(dir_path):
    name_lst = []
    entries = os.scandir(dir_path)
    for object in entries:
        if object.is_dir():
            name_lst.append(object.name)
    return name_lst


def change_dir(new_dir):
    new_dir = os.chdir(new_dir)
    return os.getcwd()


def list_files(file_path):
    name_lst = []
    entries = os.scandir(file_path)
    for object in entries:
        if object.is_file():
            name_lst.append(object.name)
    return name_lst


# program starts
running = True
while running:
    path = os.getcwd()
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    inp = int(input("\n==> "))

    if inp == 1:
        dir_list = list_dir(path)
        for object in dir_list:
            print(object)

    elif inp == 2:
        ch_dir = input("Name of directory to enter: ")
        print("Changed to", change_dir(ch_dir))
    elif inp == 3:
        file_list = list_files(path)
        for object in file_list:
            print(object, 3)
    elif inp == 4:
        break
