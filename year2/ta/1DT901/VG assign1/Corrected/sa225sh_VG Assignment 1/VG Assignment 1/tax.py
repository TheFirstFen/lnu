def tax_cal():
    income = float(input("Please provide monthly income: "))
    if income < 38000:
        tax = income * 0.3
        print(f"Corresponding income tax:  {tax}")
    elif 38000 <= income < 50000:
        första_tax = 38000 * 0.3
        andra_tax= (income-38000) * 0.35
        summan = första_tax + andra_tax
        print(f"Corresponding income tax:  {summan}")
    else:
        tax1 = 38000 * 0.3
        income -= 38000
        tax2 = 12000 * 0.35
        income -= 12000
        tax3 = income * 0.4
        tot_tax = tax1 + tax2 + tax3
        print(f"Corresponding income tax:  {tot_tax}")
tax_cal()