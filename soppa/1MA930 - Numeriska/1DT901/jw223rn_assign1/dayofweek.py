v_day = input("What day do you want to translate? ")

w_day = v_day.capitalize()

if w_day == "Monday":
    print("Måndag")
elif w_day == "Tuesday":
    print("Tisdag")
elif w_day == "Wednesday":
    print("Onsdag")
elif w_day == "Thursday":
    print("Torsdag")
elif w_day == "Friday":
    print("Fredag")
elif w_day == "Saturday":
    print("Lördag")
elif w_day == "Sunday":
    print("Söndag")
else:
    print("Error")

