actual_time = int(input("Enter the time here: "))
time_til_alarm = int(input("In how long do you want your alarm to go of in hours: "))
alarm_goes_of = float(actual_time + time_til_alarm)%24
print("The alarm goes of at {}{}".format(alarm_goes_of,'0'))