'''Problem:
Write a program fahrenheit.py that reads a The Fahrenheit temperature F (a float) from the keyboard and then print the corresponding Celsius temperature C.
The relationship between C and F is: F = (9/5)*C + 32
'''
'''Desired output examples:
Provide a temperature in Fahrenheit: 100
Corresponding temperature in Celsius is 37.77778
'''

# fahrenheit.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Converts the given temperature from Fahrenheit to Celsius with the given formula
def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (9/5) 
    return celsius

# Reads input
fahrenheit = float(input('Provide a temperature in Fahrenheit: '))

# Prints result
print('Corresponding temperature in Celsius is ', convert_fahrenheit_to_celsius(fahrenheit))
