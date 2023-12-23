import os
path = os.getcwd()


def print_sub(path):
    folder = os.scandir(path)
    for object in folder:
        if object.is_dir():                    # Check if folder
            print(object.name)
            print_sub(os.chdir(object.name))   # Call function inside function
    os.chdir("..")                             # Jump to parent folder
    return


print_sub(path)
