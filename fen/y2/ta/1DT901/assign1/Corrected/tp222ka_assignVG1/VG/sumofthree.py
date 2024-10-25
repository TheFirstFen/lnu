number = int(input("Provide a three digit number:"))

# Extract the hundreds digit
hundreds = number//100    
# Extract the tens digit
ten = (number %100)//10  
# Extract the ones digit
one = number %10
# Calculate the sum of the three digits
sumofthree = hundreds + ten + one 

print(f"Sum of digits: {sumofthree}")