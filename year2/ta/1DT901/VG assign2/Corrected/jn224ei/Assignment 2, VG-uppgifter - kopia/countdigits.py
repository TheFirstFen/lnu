n = input("Enter a large positive integer: ")
print()
zeros = 0
odds = 0
evens = 0
#  for loop checking if number is zero, even or odd
for c in n:
    if (int(c) == 0):
        zeros += 1
    elif (int(c) % 2 == 0):
        evens += 1
    elif (int(c) % 2 == 1):
        odds += 1
print("Zeros:", zeros)
print("Odd: ", odds)
print("Even: ", evens)
