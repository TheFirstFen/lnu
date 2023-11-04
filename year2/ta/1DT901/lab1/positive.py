# Read an integer and decicide if it is positive|negative|zero

n = int( input("Please provide an integer: "))

if n < 0:
    print(n, "is negative")
elif n > 0:
    print(n, "is positive")
else:
    print(n, "is zero")