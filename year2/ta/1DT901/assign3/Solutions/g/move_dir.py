import os


#  Returns a list of strings with the names of the directories
def list_dir(dir_path):
    dirs = os.scandir(dir_path)
    dir_list = []

    for d in dirs:
        if d.is_dir():
            dir_list.append(d.name)

    return dir_list


#  Returns a list of strings with the names of the files
def list_files(dir_path):
    files = os.scandir(dir_path)
    files_list = []

    for f in files:
        if f.is_file():
            files_list.append(f.name)

    return files_list


stop = True
path = os.getcwd()

while stop:
    print()
    print('1. List directories')
    print('2. Change directory')
    print('3. List files')
    print('4. Quit')
    print()
    select = int(input('==> '))

    if select == 1:
        lst = list_dir(path)

        for s in lst:
            print(s)

    elif select == 2:
        new_dir = input('Name of directory to enter: ')
        path = os.chdir(new_dir)

    elif select == 3:
        lst_files = list_files(path)

        for s in lst_files:
            print(s)

    elif select == 4:
        stop = False
