# Swedish income tax in three levels

income = int(input("Please provide monthly income: "))

local = gov = varn = 0

local = 0.3 * income

if income > 38000:
    n = income - 38000
    gov = 0.05 * n

if income > 50000:
    n = income - 50000
    varn = 0.05 * n

print("Corresponding income tax: ", round(local+gov+varn))
