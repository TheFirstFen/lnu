#Ask for a monthly income
income = int(input("Please provide a monthly income: "))


#incase of negative income ask user again
while(income < 0):
    income = int(input("Please provide a positive monthly income: "))
    

#calculate tax
if(income < 38000):
    tax = income * 0.3
    tax = round(tax)
    print(f"Corresponding income tax: {tax}")

if(income >= 38000 and income <= 50000):
    tax = (37999 * 0.3) + ((income - 37999) * 0.35)
    tax = round(tax)
    print(f"Corresponding income tax: {tax}")

if(income > 50000):
    tax = (37999 * 0.3) + (12000 * 0.35) + ((income - 50000) * 0.4)
    tax = round(tax)
    print(f"Corresponding income tax: {tax}")

