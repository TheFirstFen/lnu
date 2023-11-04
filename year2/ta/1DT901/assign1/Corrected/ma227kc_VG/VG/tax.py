income= int(input("Monthly income: "))

#30% tax
if income < 38000 :
    income *= 0.3

#35% tax for 38000 or higher and less than 50000 plus 30% tax for what is less than 38000
elif 50000 > income >= 38000:
    income = (income - 38000)*0.35 + 38000*0.3

#40% tax for what is higher than 50000 plus previously mentioned taxes
elif 50000 <= income :
    
    over_fifty = income-50000
    income = over_fifty*0.4+ ( 50000- 38000)*0.35 + 38000*0.3


print("Tax: ", income)