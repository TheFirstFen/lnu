# 8 Calculate the amount of change a person should recieve

total_cost = float(372.38)
amount_paid = float(input("Amount paid: "))  # User pays
change_amount = amount_paid - total_cost
rounded_change = round(change_amount)

# Variables
bill_1000 = 1000
bill_500 = 500
bill_200 = 200
bill_100 = 100
bill_50 = 50
bill_20 = 20
bill_10 = 10
bill_5 = 5
bill_2 = 2
coin_1 = 1

change_1000 = 0
change_500 = 0
change_200 = 0
change_100 = 0
change_50 = 0
change_20 = 0
change_10 = 0
change_5 = 0
change_2 = 0
change_1 = 0

# Calculations
if rounded_change >= bill_1000:
    change_1000 = int(rounded_change // bill_1000)
    rounded_change -= change_1000 * bill_1000

if rounded_change >= bill_500:
    change_500 = int(rounded_change // bill_500)
    rounded_change -= change_500 * bill_500

if rounded_change >= bill_200:
    change_200 = int(rounded_change // bill_200)
    rounded_change -= change_200 * bill_200

if rounded_change >= bill_100:
    change_100 = int(rounded_change // bill_100)
    rounded_change -= change_100 * bill_100

if rounded_change >= bill_50:
    change_50 = int(rounded_change // bill_50)
    rounded_change -= change_50 * bill_50

if rounded_change >= bill_20:
    change_20 = int(rounded_change // bill_20)
    rounded_change -= change_20 * bill_20

if rounded_change >= bill_10:
    change_10 = int(rounded_change // bill_10)
    rounded_change -= change_10 * bill_10

if rounded_change >= bill_5:
    change_5 = int(rounded_change // bill_5)
    rounded_change -= change_5 * bill_5

if rounded_change >= bill_2:
    change_2 = int(rounded_change // bill_2)
    rounded_change -= change_2 * bill_2

if rounded_change >= coin_1:
    change_1 = int(rounded_change // coin_1)
    rounded_change -= change_1 * coin_1

# Show results
print("Price 372.38")
print(f"Change: {round(change_amount)} kr")
print("1000kr bills:", change_1000)
print(" 500kr bills:", change_500)
print(" 200kr bills:", change_200)
print(" 100kr bills:", change_100)
print("  50kr bills:", change_50)
print("  20kr bills:", change_20)
print("  10kr coins:", change_10)
print("   5kr coins:", change_5)
print("   2kr coins:", change_2)
print("   1kr coins:", change_1)

# Done
