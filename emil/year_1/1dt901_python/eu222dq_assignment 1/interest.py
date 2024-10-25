
initial_savings = float(input("Input your savings amount here: "))
interest_rate = float(input("Input your interest rate here: "))
years_of_time = float(input("Enter the time you want to save for in years: "))
savings_after_time = initial_savings*((1+(interest_rate/100)) ** years_of_time)
round_savings = round(savings_after_time)
print(round_savings)
#Value_after_5_years = 1539