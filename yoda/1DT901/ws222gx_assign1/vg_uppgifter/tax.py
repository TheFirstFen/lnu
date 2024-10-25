income = int(input("Please provide monthly income: "))

tax = 0

# determines amount of percentage for each tax bracket
tax_rate_under_38000 = 0.3
tax_rate_38000_50000 = 0.05
tax_rate_above_50000 = 0.05

# calculates tax for income under 38000
if (income < 38000):
    tax = income * tax_rate_under_38000

# calculates tax for income between 38000 and 50000
elif (income <= 50000):
    tax = income * tax_rate_under_38000
    between_38000_50000 = income - 38000
    tax += between_38000_50000 * tax_rate_38000_50000

# calculates tax for income above 50000
else:
    tax = income * tax_rate_under_38000
    diff = income - 50000
    tax += diff * tax_rate_38000_50000
    diff = income - 38000
    tax += diff * tax_rate_above_50000

print("Corresponding income tax:", round(tax))
