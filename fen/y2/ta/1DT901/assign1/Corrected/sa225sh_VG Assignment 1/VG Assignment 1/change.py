def change(price, payment):
    if payment < price:
        print("Insufficient payment.")
        return

    change = round(payment - price)
    change_original = change  # Store the original change for printing

    bills_coins = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    change_dict = {bill: 0 for bill in bills_coins}  # Initialize dictionary to store counts

    for bill_coin in bills_coins:
        if change >= bill_coin:
            count = change // bill_coin
            change_dict[bill_coin] = count
            change -= count * bill_coin

    print(f"Change: {change_original} kr")
    for bill_coin, count in change_dict.items():
        if count > 0:
            if bill_coin >= 10:
                print(f"{bill_coin}kr bills: {count}")
            else:
                print(f"{bill_coin}kr coins: {count}")

price = float(input("Price: "))
payment = float(input("Payment: "))
change(price, payment)
