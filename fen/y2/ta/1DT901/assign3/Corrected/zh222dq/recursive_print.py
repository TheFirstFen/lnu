import os


# recursive function
def print_sub(dir_path):
    sub = ""
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_dir():
            sub += print_sub(e)
            sub += e.name + "\n"
    return sub


# Program starts
path = os.getcwd()
sub = print_sub(path)
print(sub)
