'''Problem:
Write a program alarm.py, which reads an integer corresponding to the current time (only the hour and in 24h format).
The program should then ask how many hours into the future an alarm should go off.
The program should then present the time at which the alarm will go off.
Use the modulo operator to calculate the time.
'''
'''Desired output examples:
What time is it? 14
How many hours to the alarm? 26
The alarm will go off at 16.00

What time is it? 2
How many hours to the alarm? 12
The alarm will go off at 14.00
'''
# alarm.py
# 
# Author: Samuel Berg
# Date: 26-Aug-2022

# Importing datetime library to be able to get the current hour
#import datetime

# Gets the current hour
#current_hour = datetime.datetime.now().hour

# Computes the time the alarm should go off
def calc_to_alarm_time(time_to_alarm):
    if (current_hour + time_to_alarm > 24):
        alarm_time = current_hour + (time_to_alarm % 24)
    else:
        alarm_time = current_hour + time_to_alarm
    return alarm_time

# Reads input for the current hour and time till alarm
#print(f'What time is it? {current_hour}')
current_hour = float(input('What time is it? '))
time_to_alarm = float(input('How many hours to the alarm? '))

alarm_time = calc_to_alarm_time(time_to_alarm)

# Prints the time alarm will go off
print('The alarm will go off at {:.2f}'.format(alarm_time))
