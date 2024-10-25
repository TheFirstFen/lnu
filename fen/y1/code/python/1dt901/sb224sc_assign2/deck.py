# deck.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

from random import shuffle
values = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ',
          '9 ', '10 ', 'Jack ', 'Queen ', 'King ', 'Ace ']
colors = ['of Hearts', 'of Spades', 'of Diamonds', 'of Clubs']
face_cards = ['Jack', 'Queen', 'King', 'Ace']

deck = []

for value in values:
    for color in colors:
        tmp = value + color
        deck.append(tmp)

shuffle(deck)

print('My hand:')
for i in range(5):
    print(f'{deck[i]}')
