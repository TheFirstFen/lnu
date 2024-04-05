import os
cont = True


lst = []


#  Returns a list of strings with the names of the directories
def list_dir(dir_path):
    path = os.getcwd()
    entries = os.scandir(path)
    for e in entries:
        if e.is_dir():
            lst.append(e)
    return lst


def change_dir(dir_path):
    cho2 = input("Choose directory: ")
    os.chdir(cho2)


#  Returns a list of strings with the names of the files
def list_files(dir_path):
    lst = []
    if ch == 3:
        path = os.getcwd()
        entries = os.scandir(path)
        for e in entries:
            if e.is_file():
                lst.append(e)
    return lst


# 'While' is used so the program can continue until the user decides otherwise
while cont:
    ch = int(input("1.List directories\n2.Change directory\n3.List files"
                   + "\n4.Quit\n"))

    if ch == 1:
        print(list_dir(''))
    if ch == 2:
        print(change_dir(''))
    if ch == 3:
        print(list_files(''))
    if ch == 4:
        cont = False
