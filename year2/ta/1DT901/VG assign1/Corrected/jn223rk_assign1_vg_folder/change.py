if __name__ == "__main__":
    # Fetches input from the user
    price = float(input("Price: "))
    payment = int(input("Payment: "))

    # Condition to see if payment is greater than or equal to price
    # otherwise the program ends
    if payment >= price:
        # Calculate the total change round to the nearest integer
        change = round(payment - price)
        # Calculates how many whole 1000 kr bills fits into the change
        one_thousand_whole = change // 1000
        # Then you take the remainder of the change when divided by 1000
        one_thousand_remainder = change % 1000
        # Calculates how many whole 500 kr bills fits into the change
        five_hundred_whole = one_thousand_remainder // 500
        # Then you take the remainder of the change when divided by 500
        five_hundred_remainder = one_thousand_remainder % 500
        # Calculates how many whole 200 kr bills fits into the change
        two_hundred_whole = five_hundred_remainder // 200
        # Then you take the remainder of the change when divided by 200
        two_hundred_remainder = five_hundred_remainder % 200
        # Calculates how many whole 100 kr bills fits into the change
        one_hundred_whole = two_hundred_remainder // 100
        # Then you take the remainder of the change when divided by 100
        one_hundred_remainder = two_hundred_remainder % 100
        # Calculates how many whole 50 kr bills fits into the change
        fifty_whole = one_hundred_remainder // 50
        # Then you take the remainder of the change when divided by 50
        fifty_remainder = one_hundred_remainder % 50
        # Calculates how many whole 20 kr bills fits into the change
        twenty_whole = fifty_remainder // 20
        # Then you take the remainder of the change when divided by 20
        twenty_remainder = fifty_remainder % 20
        # Calculates how many whole 10 kr bills fits into the change
        ten_whole = twenty_remainder // 10
        # Then you take the remainder of the change when divided by 10
        ten_remainder = twenty_remainder % 10
        # Calculates how many whole 5 kr bills fits into the change
        five_whole = ten_remainder // 5
        # Then you take the remainder of the change when divided by 5
        five_remainder = ten_remainder % 5
        # Calculates how many whole 2 kr bills fits into the change
        two_whole = five_remainder // 2
        # Then you take the remainder of the change when divided by 2
        two_remainder = five_remainder % 2
        # Then the remainder when divided by 2 equals the amount 1 kr bills
        one_whole = two_remainder

        print("Change: {}".format(change))
        print("1000 kr bills: {}".format(one_thousand_whole))
        print("500 kr bills: {}".format(five_hundred_whole))
        print("200 kr bills: {}".format(two_hundred_whole))
        print("100 kr bills: {}".format(one_hundred_whole))
        print("50 kr bills: {}".format(fifty_whole))
        print("20 kr bills: {}".format(twenty_whole))
        print("10 kr bills: {}".format(ten_whole))
        print("5 kr bills: {}".format(five_whole))
        print("2 kr bills: {}".format(two_whole))
        print("1 kr bills: {}".format(one_whole))
