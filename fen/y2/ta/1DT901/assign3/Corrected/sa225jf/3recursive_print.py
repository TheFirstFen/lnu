import os

# find directories and print short name and full


def print_sub(dir_path):
    all = os.scandir(dir_path)                   # scan  path
    for f in all:                                 # for all files in direcoteries
        if f.is_dir():
            print(f.name)                           # write files name
            print_sub(f.path)


path = os.getcwd()
print_sub(path)
