import os


# Function that reads the file of specified path. Then adds the lines
# of text to a list.
def read_file(file_path):
    file = open(file_path, "r")
    file_lines = []
    for line in file:
        file_lines.append(line)
    file.close()
    return file_lines


# Function that takes previously created list and writes to a file.
def write_file(lines, file_path):
    file = open(file_path, "w")
    file.writelines(lines)
    file.close()


"""
Main
"""
path = os.getcwd() + "/data/mamma_mia.txt"

lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

path = os.getcwd() + "/out/mamma out.txt"
write_file(lst, path)
print("Text saved in file", path)
