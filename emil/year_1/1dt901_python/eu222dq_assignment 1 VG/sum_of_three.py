# Input of a three digit number
digits_input = int(input("Enter your three digit number here: "))
# Calculates the first part of the number to a single digit
first_digit = int(digits_input/100)
# Calculates the second part of the number to a single digit
second_digit = int((digits_input/10)-(first_digit*10))
# Calculates the third part of the number to a single digit
third_digit = int((digits_input)-(first_digit*100)-(second_digit*10))

# Suming the digits togheter
sum_all_digits = first_digit + second_digit + third_digit
# printing the sum
print(sum_all_digits)
