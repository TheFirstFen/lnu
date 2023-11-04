# file_reader.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022

import os

'''reading(path, name):
Opens file if it exists in current directory with
the given name then reads every line into a list
which then gets printed out line by line.
'''


def reading(path, name):
    with open(path + '/' + name, 'r') as file:
        temp = file.readlines()
        print(f'Lines in file: {len(temp)}')
        print('Content of file:')
        for line in temp:
            line = line.strip('\n')
            print(line)


# Main code
path = os.getcwd()
path = path + '/out'

file_name = input('What is the name of the file to read? ')
reading(path, file_name)
