#reads an integer from user
income = int(input("Please provide monthly income: "))

#Calculates the tax, adding 5 or 10 percent to the tax above a given value
if(income > 50000):
    tax = income*0.3 + 0.05*(income - 38000) + 0.05*(income-50000)
elif(income > 38000):
    tax = income*0.3 + 0.05*(income - 38000)
else: 
    tax = income*0.3

#rounds off and prints the resulting tax
print(round(tax))