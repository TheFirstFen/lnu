import os


def print_sub(dir_path):
    entr = os.scandir(dir_path)
    for en in entr:
        if en.is_dir():
            print('\n', en.name)
            print_sub(en)


path = os.getcwd()
print('We are here:', path)
print(print_sub(path))
