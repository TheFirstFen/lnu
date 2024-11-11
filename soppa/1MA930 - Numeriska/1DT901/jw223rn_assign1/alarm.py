tim_now = int(input("What time is it? "))
hours = int(input("How many hours to the alarm? "))

tim_alarm = float((tim_now + hours) % 24)

print(f"The alarm will go off at {tim_alarm:.2f}")
