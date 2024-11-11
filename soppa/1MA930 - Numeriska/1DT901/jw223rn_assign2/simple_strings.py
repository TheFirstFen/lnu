s = input("Provide a string: ")

length = len(s)
count = 0


def first_last(s):
    first = s[0]
    last = s[length - 1]
    return first, last


def char_types(s):
    vowel = 0
    consonant = 0
    for char in s:
        if char in "aeiouyAEIOUY":
            vowel += 1
        elif char in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            consonant += 1
    return vowel, consonant


def char_symbol_number(s):
    numbers = 0
    letters = 0
    symbols = 0
    for char in s:
        asc = ord(char)
        if 48 <= asc <= 57:
            numbers += 1
        elif 65 <= asc <= 90 or 97 <= asc <= 122:
            letters += 1
        else:
            symbols += 1
    return numbers, letters, symbols


first, last = first_last(s)
vowel, consonant = char_types(s)
numbers, letters, symbols = char_symbol_number(s)

print(f'First and last in "{s}": {first} {last}')

print(f"In that sentence, the number of vowels is {vowel} and the number of \
consonants is {consonant}")

print(f'In the sentence "{s}" the number of letters is {letters}, symbols is \
{symbols} and numbers is {numbers}')
