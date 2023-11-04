# Variables Assignation
candles = 0

buy_box = 0

total_box = 0

for age in range(1, 101):
    while candles < age:  # Adding more candles if not enough
        candles += 24  # 24 candles per box
        buy_box += 1  # Keeping track of how many boxes is bought each birthday
    candles -= age

    print(f"Before birthday {age}, buy {buy_box} box(es)")  # Result

    total_box += buy_box  # Keeping track of total boxes bought

    buy_box = 0

# Total number of boxes and remaining candles
print(f"Total number of boxes: {total_box}, Remaining candles: {candles % 24}")
