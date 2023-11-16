# palindrome.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

def is_palindrome(s):
    s = s.replace(' ', '').lower()
    if s == s[::-1]:
        return True
    else:
        return False


while True:
    s = input('Please enter a string: ')
    print(f'"{s}" {is_palindrome(s)}')
