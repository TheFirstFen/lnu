three_digit_number = int(input("Provide a three digit number: "))

check_hundred = three_digit_number // 100
check_tens = (three_digit_number %100) //10
check_ones= three_digit_number %10

sum= check_hundred + check_tens + check_ones
print ("Sum of digits:", sum)
