# 7 Provide a three-digit number and calculate the sum

num = (int(input("Enter a three-digit number: ")))

if 100 <= num <= 999:
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10

    # Sum of digits
    digit_sum = digit1 + digit2 + digit3

    # Show output
    print(f"The sum of the three digits in {num} is {digit_sum}")
else:
    print("That's not a three-digit number.")

# Done
