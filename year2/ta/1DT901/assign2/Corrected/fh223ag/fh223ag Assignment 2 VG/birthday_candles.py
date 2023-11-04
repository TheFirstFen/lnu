# import math so we can round up
import math

# Variables
saved_candles = 0
age = 1
candles_needed = 0
boxes_needed = 0
candles_in_box = 24
total_boxes = 0

# make calculations and print text
for i in range(1, 101):
    candles_needed = age - saved_candles
    if candles_needed >= 1:
        boxes_needed = math.ceil(candles_needed / candles_in_box)
    saved_candles = saved_candles + ((candles_in_box * boxes_needed) - age)
    print(f"Before birthday {i}, buy {boxes_needed} box(es)")
    age += 1
    total_boxes += boxes_needed
    boxes_needed = 0

# Print the last bit of text
print(f"\n\nTotal number of boxes: {total_boxes}, ", end="")
print(f"Remaining candles: {saved_candles}")
