# eightball.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

from random import randint
magic = ['Ask again later',
         'As I see it, yes',
         'Concentrate and ask again',
         'Better not tell you now',
         'Very doubtful']

i = 'None'

while i != 'stop':
    i = input('Ask the magic 8-ball your question: ').lower()
    if i == 'stop':
        exit()
    else:
        print(f'The magic 8-ball says: {magic[randint(0, len(magic))]}')
