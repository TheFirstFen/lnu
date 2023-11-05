import os


def print_sub(dir_path, depth):

    with os.scandir(dir_path) as entries:

        for entry in entries:

            # if directory
            if entry.is_dir():
                print(depth * "   ", entry.name)
                print_sub(entry, depth+1)  # add to depth for dir in dir
            # if file
            elif entry.is_file():
                print(depth * "   ", entry.name)


# main part of the program
path = os.getcwd()
print_sub(path, 0)
