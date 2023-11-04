income = int(input("Please provide monthly income: "))

tax = 0

if income < 38000:
    tax = income * 30 / 100
    
elif 38000 < income < 50000:
    tax = (38000 * 30 / 100) + ((income - 38000) * 35 / 100)

else:
    tax = (38000 * 30 / 100) + ((12000) * 35 / 100) + ((income - 50000) * 40 / 100)
    

    
print ("Corresponding income tax:  " + str(int(tax)))

#different answers to the task, not sure how they calculated it