# birthday_candles.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

# Creating constants for maximum age and amount of candles per box
CANDLE_SIZE = 24
MAX_AGE = 100

# Creating variables for total amount of boxes, remaining candles per birthday
total_boxes = 0
remain = 0

# Computes when and how many boxes needs purchasing for each birthday
# and keeps count of remaining candles and total boxes bought
for age in range(1, MAX_AGE + 1):
    amount_box = 0
    if age > remain:
        while age > remain:
            remain += CANDLE_SIZE
            total_boxes += 1
            amount_box += 1
        print(f'Before birthday {age}, buy {amount_box} box(es)')
        remain -= age
    else:
        remain -= age

# Prints to result
print(
    f'\nTotal number of boxes: {total_boxes}, Remaining candles: {remain}')
