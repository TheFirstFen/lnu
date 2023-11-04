digits = int(input("Provide a 3 digit integer: "))
# first digit from the right
sum_of_digits = digits % 10
# middle digit
sum_of_digits += (digits % 100) // 10
# first digit from the left
sum_of_digits += (digits % 1000) // 100

print(f"Sum of digits:{sum_of_digits}")
