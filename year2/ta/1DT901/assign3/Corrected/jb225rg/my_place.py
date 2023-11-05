import os


# returns the number of directories
def count_directories(dir_path):
    no_dir = 1
    entries = os.scandir(dir_path)

    # for every directory, add and call function again
    for entry in entries:
        if entry.is_dir():
            #  print(entry.name)
            no_dir += count_directories(entry)
    return no_dir


# returns the number of files
def count_files(dir_path):
    no_fi = 0
    entries = os.scandir(dir_path)

    # if file, add 1, if directory, call function again
    for entry in entries:
        if entry.is_file():
            # print(entry.name)
            no_fi += 1
        else:
            no_fi += count_files(entry)
    return no_fi


# program start
path = os.getcwd()

# printing of resaults
print("I am here right now:", path)
print("Below me I have", count_directories(path), "directories.")
print("This directory contains", count_files(path), "files.")
