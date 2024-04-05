# file_writer.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022

import os

'''writing(path, name, content):
Opens the file that got created in the main
part of the code and writes the give content
to the file ending with a new line.
Then it requests a new string to then
recursively call the function again with the
new content till "stop" is given as the string.
'''


def writing(path, name, content):
    with open(path + '/' + name, 'a') as file:
        file.write(content + '\n')
    msg = input('> ')
    if msg == 'stop':
        exit()
    else:
        writing(path, file_name, msg)


# Main code
path = os.getcwd()
path = path + '/out'

file_name = input('Name of the file: ')
file = open(path + '/' + file_name, 'x')    # Create the file
file.close()
print('Enter the content and end with "stop":')
msg = input('> ')
writing(path, file_name, msg)
