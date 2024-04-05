import os


def print_sub(dir_path):

    with os.scandir(dir_path) as entries:
        for entry in entries:

            # if directory
            if entry.is_dir():
                print(entry.name)
                print_sub(entry)  # call function again
            # if file
            elif entry.is_file():
                print(entry.name)


# main part of the program
path = os.getcwd()
print_sub(path)
