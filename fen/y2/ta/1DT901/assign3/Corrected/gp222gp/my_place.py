import os

path = os.getcwd()
print("I am right now at:", path)


def count_directories(dir_path):
    dircounter = 0
    dirlist = os.listdir(dir_path)
    for dirs in dirlist:
        if os.path.isdir(os.path.join(dir_path, dirs)):
            dircounter += 1
    return dircounter


def count_files(dir_path):
    filecounter = 0
    filelist = os.listdir(dir_path)
    for dirs in filelist:
        if os.path.isfile(os.path.join(dir_path, dirs)):
            filecounter += 1
    return filecounter


dirprint = count_directories(path)
fileprint = count_files(path)

print("Below me are", dirprint, "directories/folders!")
print("This directory contains", fileprint, "files!")
