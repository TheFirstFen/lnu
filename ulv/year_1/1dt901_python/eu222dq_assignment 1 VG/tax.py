# input of how much a person earns.
money_earned = int(input("Enter you monthly income: "))

# only money under or equal to 38000 gets procesed here
if money_earned <= 38000:
    # the amount of money times the % of the tax
    tax = money_earned * 0.30
    # printing the amount of tax to be paid
    print(tax)
    # only money between 38000 and 50000 gets procesed here
elif 38000 < money_earned <= 50000:
    # amount to be taxed at a higer rate
    middle_tax = money_earned-38000
    # the tax for earners between 38000 and 50000
    middle_tax_final = 38000 * 0.3 + middle_tax * 0.35
    # printing the amount of tax to be paid
    print(middle_tax_final)
else:
    # amount of monet to be taxed at the higest rate
    tax = money_earned-50000
    # the tax amount for the highest earners.
    final_tax = 38000*0.3 + 12000*0.35 + tax*0.40
    # printing the amount of tax to be paid
    print(final_tax)
