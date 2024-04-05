import os

lst = []
# getcwd() was working incorrectly
# it was getting the parent folder for assignment3 instead of the wanted folder
# For the history of the code, 'read_write_old.py' can be checked
# Also I couldn't the problem with getcwd(), so I just specified the folder
path = os.getcwd() + "/assignment-03/NEW/output.txt"
file_path = os.getcwd() + "/assignment-03/NEW/New Text Document.txt"


# Enters the specified file and adds each line in it to a place in lst
def read_file(file_path):
    file = open(file_path)
    for line in file:
        lst.append(line.strip())


# Pastes the lines from lst into the specified file
def write_file(lines, file_path):
    with open(file_path, 'w') as file:
        file.write("\n".join(lines))


read_file(path)
write_file(lst, file_path)
