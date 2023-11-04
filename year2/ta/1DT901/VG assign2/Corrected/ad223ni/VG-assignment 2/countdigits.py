def count_digits(n):
    zeros = 0
    odd_digits = 0
    even_digits = 0

    # Convert the number to a string for easy digit extraction
    num_str = str(n)

    for digit in num_str:
        if digit == '0':
            zeros += 1
        elif int(digit) % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1

    print("Zeros:", zeros)
    print("Odd:", odd_digits)
    print("Even:", even_digits)


# Read the input number from the user
num = int(input("Enter a large positive integer: "))

# Call the count_digits function with the input number
count_digits(num)
