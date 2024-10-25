# Read price and payment
price = float(input("Price: "))
payment = int(input("Payment: "))

change = round(payment - price)
print("\nChange:", change, "kr")

n1000 = change // 1000
change = change % 1000
print("1000kr bills: ", n1000)

n500 = change // 500
change = change % 500
print(" 500kr bills: ", n500)

n200 = change // 200
change = change % 200
print(" 200kr bills: ", n200)

n100 = change // 100
change = change % 100
print(" 100kr bills: ", n100)

n50 = change // 50
change = change % 50
print("  50kr bills: ", n50)

n20 = change // 20
change = change % 20
print("  20kr bills: ", n20)

n10 = change // 10
change = change % 10
print("  10kr coins: ", n10)

n5 = change // 5
change = change % 5
print("   5kr coins: ", n5)

n2 = change // 2
change = change % 2
print("   2kr coins: ", n2)

print("   1kr coins: ", change)
