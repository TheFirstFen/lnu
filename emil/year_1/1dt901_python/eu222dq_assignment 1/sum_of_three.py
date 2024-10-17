digits_input = int(input("Enter your three digit number here: ")) #input of a three digit number
first_digit = int(digits_input/100) # Calculates the first part of the number to a single digit
second_digit = int((digits_input/10)-(first_digit*10))  # Calculates the second part of the number to a single digit
third_digit = int((digits_input)-(first_digit*100)-(second_digit*10)) # Calculates the third part of the number to a single digit

sum_all_digits = first_digit + second_digit + third_digit # suming the digits togheter

print(sum_all_digits) # printing the sum