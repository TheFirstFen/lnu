# Read the price and payment amount from the user
price = float(input("Price: "))
payment = float(input("Payment: "))

# Calculate the change
change = round(payment - price)

# Define the denominations of Swedish bills and coins
denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Initialize a list to store the count of each denomination
change_count = []

# Calculate the count of each denomination in the change
for denom in denominations:
    count = change // denom
    change_count.append(count)
    change -= count * denom

# Print the change amount and the count of each denomination
print("\nChange:", round(payment - price), "kr")
for i, denom in enumerate(denominations):
    print(f"{denom}kr bills/coins: {change_count[i]}")