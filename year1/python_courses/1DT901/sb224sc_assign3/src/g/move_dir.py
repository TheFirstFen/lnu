# move_dir.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022

import os

'''list_dir(dir_path):
Returns a list with all of the directories
directly below current directory.
'''


def list_dir(dir_path):
    entries = os.scandir(dir_path)
    list_of_dirs, _ = is_entries(entries)
    return list_of_dirs


'''is_entries(list_of_entries):
Returns a list with all of the directories
 and files directly below current directory.
'''


def is_entries(list_of_entries):
    dirs = []
    files = []
    for entry in list_of_entries:
        if entry.is_dir():
            dirs.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)
    return dirs, files


'''list_files(dir_path):
Returns a list with all of the files
directly below current directory.
'''


def list_files(dir_path):
    entries = os.scandir(dir_path)
    _, list_of_files = is_entries(entries)
    return list_of_files


# Main code
while True:
    print('1. List directories')
    print('2. Change directory')
    print('3. List files')
    print('4. Quit')

    n = input('\n==> ')

    # Computes what the program should do depending
    # on the user input an calls the corresponding function.
    if n == '1':
        for dirs in list_dir(os.getcwd()):
            print(dirs)
        print('\n')
    elif n == '2':
        c = input('Name of directory to enter: ')
        os.chdir(c)
        print('\n')
    elif n == '3':
        for file in list_files(os.getcwd()):
            print(file)
        print('\n')
    elif n == '4':
        exit()
