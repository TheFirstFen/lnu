#user input of income
i = int(input("Please provide monthly income: "))

if i <= 38000:
    t = i * 0.3

elif i > 38000 and i < 50000:
    t = 38000 * 0.3

    v = i - 38000

    t = (v * 0.35) + t

else:
    t = (38000 * 0.3) + (12000 * 0.35)

    v = i - 50000

    t = t + (v * 0.4)
    


#priting the results
print("Corresponting income tax:", t)
