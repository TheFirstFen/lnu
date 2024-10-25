import os


# Creating a def called print_sub with a variable which holeds the path.
# for everything in the sub_directory if it is a directiory
# the name gets printed. After every main directary is printed
# the function calls itself and prints every directary in the last
# directory.
def print_sub(path):
    sub_dir = os.scandir(path)
    for mapp in sub_dir:
        if mapp.is_dir():
            print(mapp.name)
            print_sub(mapp)


# geting the path
path = os.getcwd()
# Calling function
print_sub(path)
