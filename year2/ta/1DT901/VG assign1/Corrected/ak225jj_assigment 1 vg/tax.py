
#read input
s = int(input("Please provide monthly income: "))

#calculate income tax 
if 0 <= s < 38000:
    tax = 0.3 * s
elif 38000 <= s < 50000:
    tax = 0.3 * s + (0.05 * (s - 38000))
elif 50000 < s:
    tax =  0.3 * s + (0.05 * (s - 38000)) + (0.05 * (s - 50000))
round(tax)

#print result
print("Corresponding income tax: ", round(tax))