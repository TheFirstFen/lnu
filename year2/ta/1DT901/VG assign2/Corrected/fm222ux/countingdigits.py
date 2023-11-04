# Identifies all zeros
def zero(n):
    zero_count = 0
    for letter in num:
        if letter == "0":
            zero_count += 1
    return zero_count


# Identifies and counts all odd numbers
def odd(n):
    odd_count = 0
    for letter in num:
        if int(letter) % 2 == 1:
            odd_count += 1
    return odd_count


# Identifies and counts all even numbers
def even(n):
    even_count = 0
    for letter in num:
        if int(letter) % 2 == 0 and int(letter) != 0:
            even_count += 1
    return even_count


# Start of program
num = input("Enter a large positive integer: ")

if int(num) <= 0:
    print("This is not a positive number!")
    exit()


print(f"\nZeros: {zero(num)}")

print(f"Odd: {odd(num)}")

print(f"Even: {even(num)}")
