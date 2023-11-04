

n = int(input("Enter a large positive integer:"))
while n < 0:
    print("positive integer plz!: ")
    n = int(input("Enter a large positive integer:"))

# counters for zeros, odd digits, and even digits
zero, odd, even = 0, 0, 0

while True:
    digit = n % 10  # get the last digit in the integer
    if digit == 0:
        zero += 1   # zeros
    elif digit % 2 == 0:
        even += 1   # even num
    else:
        odd += 1    # odd num
    n = n // 10  # remove the last digit
    if n == 0:
        break  # stop the loop when all integer have been check


print(f"Zero: {zero} odds: {odd} even: {even}")
