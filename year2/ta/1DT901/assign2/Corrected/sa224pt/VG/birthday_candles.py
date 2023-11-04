box = 24  # number of candles in a box
candles = 0  # the left over candles
num_of_boxes = 0  # sum of boxes for the whole process

for age in range(1, 101):

    # check if we have enough candles for the current year
    if candles >= age:
        # deduct candles from the current year
        candles = candles - age
        print(f"Happy {age} birthday! No need to buy boxes this year!!")

    # buy more boxes of candles if needed
    else:
        boxes_needed = int((age - candles) / 24) + 1
        num_of_boxes = num_of_boxes + boxes_needed
        candles = (candles + box * boxes_needed) - age
        print(f"Before birthday {age}, buy {boxes_needed} box(es)")

# print the total number of boxes and remaining candles
print(f"Total number of boxes: {num_of_boxes}, Remaining candles: {candles}")
