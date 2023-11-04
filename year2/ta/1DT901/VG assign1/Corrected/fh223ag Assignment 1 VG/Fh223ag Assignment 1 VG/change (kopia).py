#Ask user for price and payment
price = float(input("Price: "))
payment = int(input("Payment: "))

#calculate change rounded
change = round(payment - price)
print(f"\nChange: {change}kr")

#calculate number of 1000kr bills
thousands = change // 1000
change = change - thousands * 1000
print(f"1000kr bills: {thousands}")

#500kr bills
fivehundreds = change // 500
change = change - fivehundreds * 500
print(f" 500kr bills: {fivehundreds}")

#200kr bills
twohundreds = change // 200
change = change - twohundreds * 200
print(f" 200kr bills: {twohundreds}")

#100kr bills
hundreds = change // 100
change = change - hundreds * 100
print(f" 100kr bills: {hundreds}")

#50kr bills
fifty = change // 50
change = change - fifty * 50
print(f"  50kr bills: {fifty}")

#20kr bills
twenties = change // 20
change = change - twenties * 20
print(f"  20kr bills: {twenties}")

#10kr coins
tens = change // 10
change = change - tens * 10
print(f"  10kr coins: {tens}")

#5kr coins
fives = change // 5
change = change - fives * 5
print(f"   5kr coins: {fives}")

#2kr coins
twos = change // 2
change = change - twos * 2
print(f"   2kr coins: {twos}")

#1kr coins
ones = change // 1
change = change - ones
print(f"   1kr coins: {ones}")