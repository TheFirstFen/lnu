#imports pythons math functions
import math

#reads and rounds of a float from user
price = round(float(input("Price: ")))

#reads an integer from user
money = int(input("Money: "))

#Calculates the change
change = money - price

#Calculates the minimum amount of bills and coins going from 1000kr to 1kr.
bill1000 = price//1000
price = price%1000
bill500 = price//500
price = price%500
bill200 = price//200
price = price%200
bill100 = price//100
price = price%100
bill50 = price//50
price = price%50
bill20 = price//20
price = price%20
coin10 = price//10
price = price%10
coin5 = price//5
price = price%5
coin2 = price//2
price = price%2
coin1 = price//1

#Prints the change and the amount of each bill
print("1000 bills: ", bill1000)
print("500 bills: ", bill500)
print("200 bills: ", bill200)
print("100 bills: ", bill100)
print("50 bills: ", bill50)
print("20 bills: ", bill20)
print("10 coins: ", coin10)
print("5 coins: ", coin5)
print("2 coins: ", coin2)
print("1 coins: ", coin1)
print("Change: ", change)