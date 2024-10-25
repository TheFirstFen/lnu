# Read first and last name and print shortname

first = input("First name: ")
last = input("Last name: ")
#last = last + "     "  # Hack to handle short last names. Not needed!

f = first[0]
l = last[0:4]

print("Sort name: ",f,". ",l,sep="")