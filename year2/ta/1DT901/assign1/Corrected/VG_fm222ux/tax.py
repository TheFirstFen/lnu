#Read input
income = int(input("Please provide monthly income: "))

#Conditions
if income < 38000:
    tax = int(income * 0.3)
elif 38000 <= income <= 50000:
    tax = int(income * 0.3 + (0.05 * (income-38000)))
else:
    tax = int(income * 0.3 + (0.05 * (income-38000)) + (0.05 * (income-50000)))

#Result
print(f"Corresponding income tax: {tax}")
    
    

