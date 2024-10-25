price = round(float(input("Price: ")))
payment = int(input("Payment: "))

change = payment - price

i = 0
changeArray = [1000,500,200,100,50,20,10,5,2,1]
printArray = [1000,500,200,100,50,20,10,5,2,1]

for i in range(10):
    if change >= changeArray[i]:
        oneChange = changeArray[i]
        changeArray[i] = int(change/changeArray[i])
        change = change - changeArray[i] * oneChange
        i = i + 1
    else:
        changeArray[i] = 0
        i = i + 1
i = 0

print("change: " + str (payment - price))

for i in range (10):
    print (str(printArray[i]) + "kr bills: " + str (changeArray[i]))
    i = i+1