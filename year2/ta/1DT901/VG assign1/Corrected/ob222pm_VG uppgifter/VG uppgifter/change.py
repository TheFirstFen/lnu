# read inputs
price = float(input ("Price in sek: "))
payment = int(input ("Payment in sek: "))
change = round(payment - price)

# compute and present results
# b = bill, c = coin
rest = change % payment
print("Change: ",change,"kr")

b_1000 = rest // 1000
rest = rest%1000
print ("1000 bills: ",b_1000)

b_500 = rest // 500
rest = rest%500
print("500 bills: ",b_500)

b_200 = rest // 200
rest = rest%200
print("200 bills: ",b_200)

b_100 = rest // 100
rest = rest%100
print ("100 bills: ",b_100)

b_50 = rest // 50
rest = rest%50
print ("50 bills: ",b_50)

b_20 = rest//20
rest = rest%20
print ("20 bills: ",b_20)

c_10 = rest//10
rest = rest%10
print ("10 coins: ",c_10)

c_5 = rest//5
rest = rest%5
print ("5 coins: ",c_5)

c_2 = rest//2
rest = rest%2
print ("2 coins: ",c_2)

c_1 = rest//1
print ("1 coins: ",c_1)