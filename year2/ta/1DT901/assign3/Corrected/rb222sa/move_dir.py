import os
path = os.getcwd()
task = 0


def list_dir(path):
    folder = os.scandir(path)
    lst = []
    for object in folder:
        if object.is_dir():
            lst.append(object.name)
    return lst


def list_files(path):
    folder = os.scandir(path)
    lst = []
    for object in folder:
        if object.is_file():
            lst.append(object.name)
    return lst


while task < 4:
    task = int(input("Choose option\n1. List directories\n2. Change directory"
                     "\n3. List files\n4. Quit\n"))
    print()
    if task == 1:
        for i in list_dir(path):
            print(i)
    if task == 2:
        folder = input("Name of directory to enter: ")
        path = os.chdir(folder)
    if task == 3:
        for i in list_files(path):
            print(i)
    print()
