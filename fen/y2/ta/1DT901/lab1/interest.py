# Compute 5-year interest

# Read savings (int) and interest (int)
savings = int( input("Initial savings: "))
rate = int( input("Interest rate (in percentages): "))
years = int( input("Number of years: "))

# Compute result
r = 1 + rate/100
result = r**years * savings
result = round(result)

print(f"\nThe value of your savings after {years} years is {result}")
