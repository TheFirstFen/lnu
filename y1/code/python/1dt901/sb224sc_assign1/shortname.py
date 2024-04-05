'''Problem:
Write a program shortname.py, reading a first name, a middle name and a last name (given name and family name) as strings.
The output should consist of the first letter of the first name followed by a dot and a space, 
first letter of the middle name followed by a dot and a space and then followed by the first four letters of the last name. 
'''
'''Desired output examples:
First name: Jabba  
Middle name: Desilijic
Last name: Tiure
Short name: J. D. Tiur
'''

# shortname.py
# 
# Author: Samuel Berg
# Date: 27-Aug-2022

# Computes a shortened version of given fullname according to specifications and prints it
def name_shortener(first_name, middle_name, last_name):
    print(f'Short name: {first_name[0]}. {middle_name[0]}. {last_name[0:4]}')

# Reads input
first_name = input('First name: ').capitalize()
middle_name = input('Middle name: ').capitalize()
last_name = input('Last name: ').capitalize()

# Calls func name_shortener
name_shortener(first_name, middle_name, last_name)
