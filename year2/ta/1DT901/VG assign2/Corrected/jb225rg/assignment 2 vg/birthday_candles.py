
candle = 0          # candles
box = 24            # box of candles
counter_b = 0       # counts boxes
age = 100
cby = 0             # (current birthday)

for i in range(1, age + 1):  # 1 to 100

    if candle < i:   # if less candles than age
        cbr = 0

        while candle < i:   # buy boxes until enough for age
            candle = candle + box
            counter_b += 1
            cbr += 1

        # print boxes baught
        print(f"Before birthday {i}, buy", cbr, "box(es)")
        candle = candle - i      # remove used candles

    elif candle >= i:     # if already enough candles
        print(f"Before birthday {i}, you already have enough, no new" +
              "box needed")
        candle = candle - i

# print total and leftover
print("Total number of boxes:", counter_b, "Remaining candles:", candle)
