'''Problem:
Write a program that translates weekdays to another language.
The user should provide a day in the week in English and get it translated to the other language.
If the user writes an unknown day, the program should give an error.
Assume correct upper/lower first case -- upper in English and lower in Swedish (for example, you can use any two languages)
'''
'''Desired output examples:
What day would you like to translate? Thursday
Torsdag
'''

# dayofweek.py
#
# Author: Samuel Berg
# Date: 27-Aug-2022

# Links the english words for the all the days of the weeks names with the corresponding swedish ones
dictionary = {
    'Monday': 'Måndag',
    'Tuesday': 'Tisdag',
    'Wednesday': 'Onsdag',
    'Thursday': 'Torsdag',
    'Friday': 'Fredag',
    'Saturday': 'Lördag',
    'Sunday': 'Söndag'
}

translate = input('What day would you like to translate? ').capitalize()

# Prints result or gives an error message if incorrect day entered
print(dictionary.get(translate, 'Please provide an actual day of the week in english.'))
