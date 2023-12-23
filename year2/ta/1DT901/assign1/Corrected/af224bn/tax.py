# 14 Read a (positive) income and calculate tax

income = float(input("Enter your monthly income in SEK: "))

tax_rate_1 = 0.30  # 30%
tax_rate_2 = 0.35  # 35%
tax_rate_3 = 0.40  # 40%

# If user inputs negative income
if income <= 0:
    print("Please provide a positive income")

elif income < 38000:
    tax = income * tax_rate_1
    print("Corresponding income tax", tax)

elif income <= 50000:
    tax = 38000 * tax_rate_1 + (income - 38000) * tax_rate_2
    print("Corresponding income tax", tax)

else:
    tax = 38000 * tax_rate_1 + 12000 * tax_rate_2 + (income - 50000) * tax_rate_3
    print("Corresponding income tax", tax)

# Done
