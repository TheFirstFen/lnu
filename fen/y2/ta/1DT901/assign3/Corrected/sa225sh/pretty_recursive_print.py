import os


def print_sub(dir_path, depth):
    dir_lst = [d for d in os.listdir(dir_path)
               if os.path.isdir(os.path.join(dir_path, d))]
    for elem in dir_lst:
        print(" " * depth * 4, end="")
        print(elem)
        ny = os.path.join(dir_path, elem)
        print_sub(ny, depth + 1)


path = os.getcwd()
depth = 0
print_sub(path, depth)
