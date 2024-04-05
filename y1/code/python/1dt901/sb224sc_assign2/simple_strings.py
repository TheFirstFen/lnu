# simple_strings.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

def first_last(s):  # Returns the first and last character in the string s
    return print(f'First and last in "{s}": {s[0]} {s[-1]}')


def char_types(s):  # Returns the number of vowels and consonants in string s
    vowel = 0
    consonants = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels:
            vowel += 1
        else:
            consonants += 1
    return print(f'In that sentence, the number of vowels is {vowel} and the' +
                 f'number of consonants is {consonants}')


# Returns the number of characters,
# symbols (including spaces) and numbers in string s
def char_symbol_number(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = [' ', '.', ',', '!', '?', '"', "'", '&']
    num = 0
    symbol = 0
    letter = 0
    for i in s:
        if i in numbers:
            num += 1
        elif i in symbols:
            symbol += 1
        else:
            letter += 1
    return print(f'In the sentence "{s}" the number of letters is {letter}, ' +
                 f'symbols is {symbol} and numbers is {num}')


s = 'I am 1 with the Force, not 2...'

first_last(s)
char_types(s)
char_symbol_number(s)
