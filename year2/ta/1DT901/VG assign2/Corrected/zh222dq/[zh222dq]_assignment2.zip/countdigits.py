# Funktion för att lista ut zero, odd, even
def digits(d):
    zero = 0
    odd = 0
    even = 0

    while d > 0:
        digit = d % 10
        # Räknar antalet nollor
        if digit == 0:
            zero = zero + 1
        # Räknar antalet udda nummer
        elif digit % 2 != 0:
            odd = odd + 1
        # Räknar antalet jämna nummer
        else:
            even = even + 1
        d = d // 10
    return zero, odd, even


# Start of program
n = int(input("Enter a large positive integer: "))

# Retunera till funktionen
zero, odd, even = digits(n)

print("Zeros:", zero)
print("Odd:", odd)
print("Even:", even)
