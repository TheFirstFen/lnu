import math

# Constant
BOX = 24

# Keep track of candles, boxes, and total boxes bought
candle = 0
boxes = 0
buy_boxes = 0

# Loop over each year from 1 to 100
for year in range(1, 101):
    # Calculate how much candle needed for current year
    candle_need = year

    # Buy candle box if not enough candles
    if candle < candle_need:
        # Calculate how many additional boxes are needed
        # Rounding up to the nearest whole box
        # Credit to TA
        boxes = math.ceil((year - candle) / BOX)

        # Calculating how much candle remaing left for the current year
        # Update 'candle' with the remaining candles
        candle = (boxes * BOX) - candle_need + candle

        # Increment boxes bought
        buy_boxes += boxes
        print(f"Before birthday {year}, buy {boxes} box(es)")
    else:
        # Enough candles for the current year
        candle -= candle_need

print(f"Total number of boxes: {buy_boxes}, Remaining candles: {candle}")
