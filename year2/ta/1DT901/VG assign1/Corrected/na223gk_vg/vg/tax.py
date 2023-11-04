var = int(input("Please provide monthly income: "))
tax = 0
# Calculate the tax amount and print it out.
if var <= 38000 : 
    tax = round(var * 0.30)
    print(tax, "kr")
elif  38000 <= var <= 50000:
    tax = round(38000 * 0.3 + (var  - 38000) * .35) 
    print(tax,"kr")
else:
    tax = round(38000 * 0.3 + 12000 * .35 + (var - 50000) * .4)
    print(tax,"kr")
# monthly_income = float(input("Enter your monthly income: "))

# # Calculate the income tax owed
# if monthly_income <= 38000:
#   tax = monthly_income * 0.3
# elif monthly_income <= 50000:
#   tax = 38000 * 0.3 + (monthly_income - 38000) * 0.35
# else:
#   tax = 38000 * 0.3 + 12000 * 0.35 + (monthly_income - 50000) * 0.4

# # Print the income tax
# print("Your income tax is:", tax)