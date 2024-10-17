price = float(input("Enter the prize: "))       #Price, 
payment = float(input("Enter the payment: "))   #payment
cash = round(payment - price)                   #Money to be returned 

cash_1000 = (cash//1000)                        #amount of hole 1000kr bills
cash1 = cash%1000                               #amount left after the 1000kr bills

cash_500 = (cash1//500)                         #same as above but with different values on bills and coins.
cash2 = cash1 % 500

cash_200 = (cash2//200)
cash3 = cash2%200

cash_100 = (cash3//100)
cash4 = cash3%100

cash_50 = (cash4 // 50)
cash5 =cash4 % 50

cash_20 = (cash5//20)
cash6 = cash5%20

cash_10 = (cash6 // 10)
cash7 = cash6 % 10

cash_5 = (cash7//5)
cash8 = cash7%5

cash_2 =(cash8//2)
cash9 = cash8%2

cash_1 = (cash9//1)
cash10 = cash9%1 

print("1000kr bills: {}".format(cash_1000))     #printing what bill and then the amount of that bill
print("500kr bills: {}".format(cash_500))
print("200kr bills: {}".format(cash_200))
print("100kr bills: {}".format(cash_100))
print("50kr bills: {}".format(cash_50)) 
print("20kr bills: {}".format(cash_20)) 
print("10kr coins: {}".format(cash_10)) 
print("5kr coins: {}".format(cash_5))
print("2kr coins: {}".format(cash_2))
print("1kr coins: {}".format(cash_1))