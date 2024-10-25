import os

lst = []
path = os.getcwd()+"/NEW/New Text Document.txt"


# Enters the specified file and adds each line in it to a place in lst
def read_file(file_path):
    file = open(file_path)
    for line in file:
        lst.append(line.strip())


# Prints the lines from lst
def write_file(lines, file_path):
    for line in lines:
        print(line)


read_file(path)
write_file(lst, path)
