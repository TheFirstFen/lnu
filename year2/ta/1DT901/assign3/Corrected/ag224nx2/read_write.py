import os


def read_file(file_path):
    lstLine = []

    with open(file_path, 'r') as infile:
        r = 0

        for row in infile:
            r += 1
            row = row.rstrip()
            lstLine.append(row)

    return lstLine


def write_file(lista, file_path):
    with open(file_path, 'w') as outfile:
        for i in range(0, len(lista)):
            outfile.write(lista[i] + '\n')


# program starts
path = os.getcwd() + '/live.py/live4.py/data/pinkfloyd.txt'
lst = read_file(path)
lines = len(lst)
print(f'Read {lines} lines from file {path}')

path = os.getcwd() + '/live.py/live4.py/data/pinkfloydOut.txt'
Writen = write_file(lst, path)
print('Output of text saved in file: ', path)
