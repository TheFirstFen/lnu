# reading_star_wars.py
#
# Author: Samuel Berg
# Date: 05-Oct-2022

import os
import Character

# Main code
path = os.getcwd()
file = '/data/starwars.txt'
counter = 0
person = f'p{counter}'

with open(path + file, 'r') as f:
    print('A Collection of Star Wars Characters:')
    for line in f:
        line = line.strip('\n')
        line = line.split(', ')
        person = Character.Character(line[0], line[1], line[2])
        print(person.get_name(), ' ' * (22 - len(person.get_name())),
              person.get_kind(), ' ' * (14 - len(person.get_kind())),
              person.get_planet())
        counter += 1
