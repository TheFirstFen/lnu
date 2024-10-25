money_earned = int(input("Enter you monthly income: ")) # input of how much a person earns.

# mindre pängar än 32000 ge tax på 30%
#mellan 38k och 50k lägg 35% tax på summan mellan
#Allt över 50k ska ha en tax på 40%

if money_earned<=38000:             #only money under or equal to 38000 gets procesed here
    tax = money_earned*.30          # the amount of money times the % of the tax
    print(tax)                      # printing the amount of tax to be paid
elif 38000<money_earned<=50000:     #only money between 38000 and 50000 gets procesed here
    middle_tax = money_earned-38000     # amount to be taxed at a higer rate
    middle_tax_final =38000*0.3 + middle_tax*0.35  #the tax for earners between 38000 and 50000
    print(middle_tax_final)             #printing the amount of tax to be paid
else:
    tax = money_earned-50000            #amount of monet to be taxed at the higest rate
    final_tax = 38000*0.3 + 12000*0.35 + tax*0.40   #the tax amount for the highest earners.
    print(final_tax)                   #printing the amount of tax to be paid