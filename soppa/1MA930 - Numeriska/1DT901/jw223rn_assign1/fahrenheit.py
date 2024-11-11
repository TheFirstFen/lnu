fahr = int(input("Provide a temperature in fahrenheit: "))

c = (fahr-32)*(5/9)
rc = round(c, 5)

print(f"Corresponding temperature in celsius is {rc}")
