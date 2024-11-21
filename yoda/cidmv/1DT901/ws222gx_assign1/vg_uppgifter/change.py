price = float(input("Price: "))
payment = float(input("Payment: "))

change = round(payment-price)
print("Change: ", change)

# singles out the first digit from change
rest = change % 10
change -= rest
print(change)
# five crown
five_coins = rest//5
rest %= 5

# two crown
two_coins = rest//2
rest %= 2

# one crown
one_coins = rest

# singles out the second digit from change
rest = change % 100
change -= rest

# 50 crown
fifty_banknotes = rest//50
rest %= 50

# 20 crown
twenty_banknotes = rest//20
rest %= 20
ten_coins = rest

# singles out the third digit from change
rest = change % 1000
change -= rest

# 500 crown
five_hundred_banknotes = rest // 500
rest %= 500

# 200 crown
two_hundred_banknotes = rest // 200
rest %= 200

# 100 crown
hundred_banknotes = rest//100

# 1000 crown
rest = change % 10000
thousand_banknotes = rest // 1000

# prints out the result
print(f"""
1000kr bills: {thousand_banknotes}
 500kr bills: {five_hundred_banknotes}
 200kr bills: {two_hundred_banknotes}
 100kr bills: {hundred_banknotes}
  50kr bills: {fifty_banknotes}
  20kr bills: {twenty_banknotes}
  10kr coins: {ten_coins}
   5kr coins: {five_coins}
   2kr coins: {two_coins}
   1kr coins: {one_coins}
""")
