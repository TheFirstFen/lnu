
 # Read monthly income from the user
income = int(input("Please provide monthly income: "))

# Calculate the income tax
if income < 38000:
    tax = income * 0.3
elif income <= 50000:
    tax = 38000 * 0.3 + (income - 38000) * 0.35
else:
    tax = 38000 * 0.3 + 12000 * 0.35 + (income - 50000) * 0.4

# Print the corresponding income tax
print("Corresponding income tax:", tax)
