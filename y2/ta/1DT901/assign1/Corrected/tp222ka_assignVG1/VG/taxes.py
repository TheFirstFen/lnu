user_income = int(input("Please provide monthly income: "))

# Calculate the total tax based on income and tax rates
# 30% tax all below 38,000kr/ month 
# +5% tax all income in the interval 38,00- 50,000kr. 
# +5% tax on all income above 50,000kr 
if 0 <= user_income <=38000: 
    total_tax = user_income * 0.3
    print("Corresponding income tax: ", round(total_tax))
elif 38000 <= user_income <=50000: 
    total_tax = ((user_income-38000)*0.35) + 38000*0.3
    print("Corresponding income tax: ", round(total_tax))
else: 
    total_tax = (((50000-38000)*0.35) + 38000*0.3)+((user_income-50000)*0.4)
    print("Corresponding income tax: ", round(total_tax))