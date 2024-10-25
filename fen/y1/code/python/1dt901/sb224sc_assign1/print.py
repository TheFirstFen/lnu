'''Problem:
Write a program print.py that prints the phrase Knowledge is power!
on one line, on three lines, one word on each line,
inside a rectangle made up by the characters = and |.
'''
'''Desired output examples:
Knowledge is power!

Knowledge
   is
  Power!

=========================
|                       |
|  Knowledge is power!  |
|                       |
=========================
'''

# print.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Prints the result
print('Knowledge is power!')

print('\nKnowledge\n   is\n  Power!')

print('\n=========================\n'
      + '|                       |\n'
      + '|  Knowledge is power!  |\n'
      + '|                       |\n'
      + '=========================')
