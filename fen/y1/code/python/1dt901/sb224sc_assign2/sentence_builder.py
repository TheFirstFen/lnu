# sentence_builder.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022
from random import randint
PRONOUN = ['It', 'They', 'You', 'I', 'We']
VERB = ['will see', 'will eat', 'will pull', 'will touch', 'will paint']
NOUN = ['a house', 'a car', 'a computer', 'a tree', 'an elephant']


def pronoun() -> str:
    var = randint(0, 4)
    return PRONOUN[var]


def verb() -> str:
    var = randint(0, 4)
    return VERB[var]


def noun() -> str:
    var = randint(0, 4)
    return NOUN[var]


for _ in range(10):
    print(f'{pronoun()} {verb()} {noun()}')
