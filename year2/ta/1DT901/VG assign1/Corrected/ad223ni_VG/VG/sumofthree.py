# Write a three digit number
number = int(input("Provide a three digit number: "))

# Calculate the three numbers using integer division and remainder
hundratal = number // 100
tiotal = (number % 100) // 10
ental = number % 10

# Calculate the sum of the three numbers
summa = hundratal + tiotal + ental 

# Print the results
print("Sum of digits", summa) 


