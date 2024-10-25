import os


def read_file():
    print(' ', end='')
    readlist = []
    file = open(path, "r")
    for line in file:
        print(line, end=' ')
        readlist.append(line)
    file.close()
    return readlist


def write_file(lines, file_path):
    full_text = lines
    file = open(file_path, "w")
    for items in range(0, len(lines)):
        file.write(full_text[items])
    file.close()


path = os.getcwd() + "/mamma_mia.txt"

lst = read_file()
print(f"Read {len(lst)} lines from file {path}")

path = os.getcwd() + "/output.txt"
write_file(lst, path)
print("Text saved in file", path)
