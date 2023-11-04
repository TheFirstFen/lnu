income= int(input("Please provide monthly income: "))

if income <=38000:  tax = income *0.3
elif income <=50000: 
    tax = 38000 * 0.3 
    tax+= (income - 38000) * 0.35
else : 
    tax = 38000 * 0.3 
    tax+= (50000 - 38000) * 0.35
    tax+= (income - 50000) * 0.4
print (f"Corresponding income tax: {tax}")