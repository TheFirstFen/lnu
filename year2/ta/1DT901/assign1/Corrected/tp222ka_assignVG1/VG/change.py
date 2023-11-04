price = float(input("Price: "))
payment = int(input("Payment:"))

# Calculate the total change
change = round(payment - price)
print(f"Change: {change}kr")


# Calculate the quantity of each bill/coin denomination in the change
tusen = change // 1000          # Number of 1000kr bills
change %= 1000
five_hundred = change // 500     # Number of 500kr bills
change %= 500
two_hundred = change // 200      # Number of 200kr bills
change %= 200
hundred = change // 100          # Number of 100kr bills
change %= 100
fifty = change // 50             # Number of 50kr bills
change %= 50
tweenty = change // 20           # Number of 20kr bills
change %= 20
teen = change // 10              # Number of 10kr coins
change %= 10
five = change // 5               # Number of 5kr coins
change %= 5
two = change // 2                # Number of 2kr coins
change %= 2
one = change // 1                # Number of 1kr coins

# Display the quantity of each bill/coin 
print(f"1000kr bills:{tusen}\n",
    f"500kr bills:{five_hundred}\n",
    f"200kr bills:{two_hundred}\n",
    f"100kr bills:{hundred}\n",
    f"50kr bills:{fifty}\n",
    f"20kr bills:{tweenty}\n",
    f"10kr bills:{teen}\n",
    f"5kr bills:{five}\n",
    f"2kr bills:{two}\n",
    f"1kr bills:{one}\n",)
    