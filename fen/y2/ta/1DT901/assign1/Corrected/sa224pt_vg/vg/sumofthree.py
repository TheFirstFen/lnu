digits = int (input("Provide a three digit number: "))

first_digit = int (digits / 100) # to get the first digit to the left
second_digit = int (digits / 10 - (first_digit * 10)) # to get the second digit to the left
third_digit = int (digits - int(digits / 10)*10) # to get the third digit to the left

print("Sum of digits: " + str(first_digit+second_digit+third_digit))