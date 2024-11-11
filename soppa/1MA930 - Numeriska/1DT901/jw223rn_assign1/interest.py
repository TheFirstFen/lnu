s = int(input("Initial savings: "))
p = int(input("Interest rate (in percentages): "))
y = int(input("Number of years "))

pro_p = (1 + p/100)


savings = s * (pro_p ** y)


rsavings = round(savings)

print(f"The value of your savings after {y} years: {rsavings}")