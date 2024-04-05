if __name__ == "__main__":
    monthly_income = int(input("Please provide monthly income: "))
    # Calculates the base tax for all income
    monthly_tax_base = monthly_income * 0.3
    monthly_tax = monthly_tax_base

    # Checks whether the income is greater than or equal to 38000
    # and lesser than or eqaul to 50000
    # then add an extra 5% tax to the income over 38000
    if monthly_income >= 38_000 and monthly_income <= 50_000:
        monthly_tax += (monthly_income - 38_000) * 0.05
    # If the income is greater than 50000
    # then add an extra 5% tax to the income over 50000
    elif monthly_income > 50_000:
        monthly_tax += (monthly_income - 50_000) * 0.05

    taxes = "Corresponding income tax: {}".format(round(monthly_tax))
    print(taxes)
