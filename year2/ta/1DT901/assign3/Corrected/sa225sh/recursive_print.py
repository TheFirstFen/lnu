import os


def print_sub(dir_path):
    dir_lst = [d for d in os.listdir(dir_path)
               if os.path.isdir(os.path.join(dir_path, d))]
    for elem in dir_lst:
        print(elem)
        ny = os.path.join(dir_path, elem)
        print_sub(ny)


path = os.getcwd()
print_sub(path)
