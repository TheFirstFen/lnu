print()
price = float(input("Enter the price of the article:  "))
print()
payment = float(input("Enter the note that you are paying with:  "))
print()
change = round(payment - price)
print()
print("Change: ",change,"kr")

print()
print()

#bill_1000kr
if change >= 1000: 
    print("1000kr bills: ",(change // 1000)) 
else: print("1000kr bills: ", 0)
print()
# bill_500kr 
if (change % 1000) >= 500:
    print("500kr bills: ",((change % 1000) // 500))
else: print("500kr bills:  ", 0)
print()
# bill_200kr 
if (((change % 1000) % 500)) >= 200:
    print("200kr bills: ", (((change % 1000) % 500) // 200))
else: print("200kr bills: ",0)
print()
# bill_100kr 
if ((((change % 1000) % 500) % 200)) >= 100:
    print("100kr bills: ", ((((change % 1000) % 500) % 200)) // 100)
else: print("100kr bills: ",0)
print()
# bill_50kr 
if ((((change % 1000) % 500) % 200) % 100) >= 50:
    print("50kr bills:  ", (((((change % 1000) % 500) % 200)) % 100) // 50)
else: print("50kr bills:  ",0)
print()
# bill_20kr 
if (((((change % 1000) % 500) % 200) % 100) % 50) >= 20:
    print("20kr bills: ", ((((((change % 1000) % 500) % 200)) % 100) % 50) // 20)
else: print("20kr bills:  ",0)
print()
# bill_10kr 
if ((((((change % 1000) % 500) % 200) % 100)% 50) % 20 ) >= 10:
    print("10kr coins:  ", (((((((change % 1000) % 500) % 200)) % 100) % 50) % 20) // 10)
else: print("10kr coins: ",0)
print()
# coin_5kr 
if (((((((change % 1000) % 500) % 200) % 100)% 50) % 20) % 10) >= 5:
    print("5kr coins:  ", ((((((((change % 1000) % 500) % 200)) % 100) % 50) % 20) % 10) // 5)
else: print("5kr coins:  ",0)
print()
# coin_2kr 
if ((((((((change % 1000) % 500) % 200) % 100)% 50) % 20) % 10) % 5) >= 2:
    print("2kr coins:  ", (((((((((change % 1000) % 500) % 200)) % 100) % 50) % 20) % 10) % 5) // 2)
else: print("2kr coins:  ",0)
print()
# coin_1kr 
if (((((((((change % 1000) % 500) % 200) % 100)% 50) % 20) % 10) % 5) % 2) >= 1:
    print("1kr coins:  ", ((((((((((change % 1000) % 500) % 200)) % 100) % 50) % 20) % 10) % 5) % 2 ) // 1)
else: print("1kr coins:   ",0)
print()