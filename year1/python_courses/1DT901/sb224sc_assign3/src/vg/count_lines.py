# count_lines.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022

import os

'''count_py_lines(dir_path):
For every file in every directory below current directory
pass it if it starts with a "." and if it ends with ".py"
open the file and read each line into an index in a list
and if index in list is empty or new line character only
remove it. Then we compute the length of the modified list
and do that for each file ending with ".py" to then return
total amount of actual lines of python code below current directory.
'''


def count_py_lines(dir_path):
    count = 0
    for subdir, _, files in os.walk(dir_path):
        for file in files:
            if file.startswith('.'):
                pass
            else:
                if file.endswith('.py'):
                    with open(f'{subdir}/{file}', 'r', encoding='utf-8') as f:
                        temp = f.readlines()
                        for line in temp:
                            if line == '\n' or line == '':
                                temp.remove(line)
                        count += len(temp)
    return count


# Main code
os.chdir('..')
path = (os.getcwd())

print(count_py_lines(path))
