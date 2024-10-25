from math import ceil

candles = 0
box_count = 0

for year in range(1, 101):
    if candles < year:
        to_buy = ceil((year - candles)/24)
        print(f"Before birtday {year}, buy {to_buy} box(es)")
        candles = candles + to_buy*24

        box_count += to_buy
    candles = candles - year

print("\nTotal number of boxes", box_count, ", remaining candles",  candles)
