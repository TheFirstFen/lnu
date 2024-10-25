name = input("Enter your name here: ") 
middle_name = input("Enter your middle name here: ")
last_name = input("Enter your last name here: ")

name_cap = name.capitalize()
middle_cap = middle_name.capitalize()
last_cap = last_name.capitalize()

name_short = name_cap[:1]
middle_name_short = middle_cap[:1]
last_name_short = last_cap[:4]

x, y, z = name_short, middle_name_short, last_name_short
print(x+". "+y+". "+z)