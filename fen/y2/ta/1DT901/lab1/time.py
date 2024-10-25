# Read seconds, provide hours,mintus, and seconds

time = int( input("Give anumber of seconds: "))

hours = time//3600
time = time%3600   # Remove hours

minutes = time//60
time = time%60   # Remove minutes

seconds = time

print("This corresponds to:", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")

