
n = input("Please enter a series of integers: ")

z = 0     # start variables
e = 0
o = 0

for s in n:
    if int(s) == 0:  # if zero
        z += 1       # adds one to the counter
    elif int(s) % 2 == 0:    # if even
        e += 1
    else:            # if the number isn't a zero or even, it has to be odd
        o += 1

# print results
print("zeros:", z, "even:", e, "odd:", o)
