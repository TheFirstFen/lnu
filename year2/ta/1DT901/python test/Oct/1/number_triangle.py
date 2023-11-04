n = int(input("Number of rows in the triangle in range 1-9: "))

if n < 1 or n > 9:
    print("Number must be in range 1-9!!!")
    exit()

for i in range(1, n+1):
    ws = n-i   # Number of white space
    dig = i    # Digits to print
    print(" "*ws, end="")       # Initial whitespace
    for j in range(1, dig+1):   # Numbers 123...
        print(j, end="")
    print()                     # Break line
