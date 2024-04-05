import os
lst_s = []
path_read = os.getcwd() + "/mamma_mia.txt"
path_write = os.getcwd() + "/mamma_mia_write.txt"


# Function called read_file
def read_file(file_path):
    file = open(file_path, "r")
    for line in file:
        lst_s.append(line)
    file.close()


def write_file(lines, file_path):
    file = open(path_write, "w")
    for i in lines:
        file.write(i)
    file.close()


read_file(path_read)
write_file(lst_s, path_write)
