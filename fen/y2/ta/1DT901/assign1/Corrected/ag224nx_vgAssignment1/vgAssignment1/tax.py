income = int(input('Din inkomst (i siffror):'))

#skatt-raknare
extra1 = income * 0.3
extra2 = (income - 37999) * 0.05
extra3 = (income - 49999) * 0.05
a1 = round(extra1)
a2 = round(a1 + extra2)
a3 = round(a2 + extra3)

if income < 38000 and income > 0:
    print('Skatt:', a1, 'kr')
elif income >= 38000 and income < 50000:
    print('Skatt', a2, 'kr')
else:
    if income >= 50000:
        print('Lite for mycket pengar, skatt:', a3, 'kr')
    else:
        print('Sluta vara pank')