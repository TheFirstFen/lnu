intal_savings = int(input("Initial savings: "))
intrest_rate_percentage = int(input("Intrest rate (in percentages): "))
number_of_years = int(input("Number of years: "))

decimal_percentage = (intrest_rate_percentage/100)+1

value = round(intal_savings*decimal_percentage**number_of_years)
print(f"The value after your savings after {number_of_years} is {value}")
