# An exercise solved in two different ways

s = input("Enter a large positive integer: ")
n = int(s)

if n < 1:
    print("The number must be positive!")
    exit()

# Input as a string (Alternative 1)
odd, even, zero = 0, 0, 0
for c in s:
    p = int(c)
    if p == 0:
        zero += 1
    elif p % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nZeros:", zero, "\nOdd:", odd, "\nEven:", even)

# Input as an integer (Alternative 2)
odd, even, zero = 0, 0, 0
while n > 0:
    p = n % 10   # Pick last
    n = n // 10  # Remove last
    if p == 0:
        zero += 1
    elif p % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nZeros:", zero, "\nOdd:", odd, "\nEven:", even)
