# morse.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022


# Main code
'''
Created a dictionary for each alphabetic character as keys
and there morse code equivalents as the values.
'''
morse_dict = {
    'a': '.-', 'k': '-.-', 'u': '..-',
    'b': '-...',  'l': '.-..',  'v': '...-',
    'c': '-.-.',  'm': '--',    'w': '.--',
    'd': '-..',   'n': '-.',    'x': '-..-',
    'e': '.',     'o': '---', 'y': '-.--',
    'f': '..-.',  'p': '.--.',  'z': '--..',
    'g': '--.',   'q': '--.-', 'å': '.--.-',
    'h': '....',  'r': '.-.',   'ä': '.-.-',
    'i': '..',    's': '...',   'ö': '---.',
    'j': '.---', 't': '-'
}

# Alphabetic string should be entered and you will get
# the morse code equivalent back
msg = input('Write a message: ').lower()
print('Message in Morse code:')
for letter in msg:
    if letter == ' ':
        print(' ', end=' ')
    else:
        print(morse_dict[letter], end=' ')
print('')

# Exchanges the keys and the values through out given dictionary
morse_dict = dict([(value, key) for key, value in morse_dict.items()])

# Morse string should be entered and you will get
# the alphabetic equivalent back
msg = input('Write in Morse code: ')
print('Message in plain language:')
for i in msg.split(' '):
    if i == '':
        print('', end='')
    else:
        print(morse_dict[i], end=' ')
print('')
