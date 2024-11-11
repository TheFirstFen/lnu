income = int(input("Please provide monthly income: "))      #asks the user for its monthly income

u_tax = income * 0.3                            #Calculates 30% tax if its under 38k
tax_38 = 38000 * 0.3                            #calculates 30% tax off the first 38k if the income is higher
m_tax = (income - 38000) * 0.35                 #Removes the first 38k to apply the 35% tax on the rest 
tax_50 = (38000 * 0.3) + (12000 * 0.35)         #Store the taxes paid on the first 50k if the income is higher
o_tax = (income - 50000) * 0.4                  #Applies the 40 % tax on the icome above 50k


if income < 38000:
    print(f"Corresponding income tax: {int(u_tax)}")                #If income is below 38k, print the calculated tax u_tax
elif 38000 <= income < 50000:
    print(f"Corresponding income tax: {int(tax_38 + m_tax)}")       #if income between 38k and 50k prints taxes on the first 38k then adds the taxes off the rest of income
else:
    print(f"Corresponding income tax: {int(tax_50 + o_tax)}")       #prints the 30% tax on 38k plus 35% tax on the income between 38k and 50k plus 40% tax on the income above.