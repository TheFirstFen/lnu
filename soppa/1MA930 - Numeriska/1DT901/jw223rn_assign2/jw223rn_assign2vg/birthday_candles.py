# Creating variables
bday = 0
candles = 0
boxes = 0
newbox = 0
candles_left = 0

# For loop that checks each birthday up to 100
for bday in range(0, 101):
    while candles < bday:        # Adds a new box of candles if needed
        boxes += 1
        newbox += 1
        candles += 24
    if candles >= bday:
        if newbox == 0:          # If no new box was needed then dont print
            newbox = 0
            candles = candles - bday
        else:                    # If new box was needed print how many of them
            print(f"Before birthday {bday}, buy {newbox} box(es)")
            newbox = 0
            candles = candles - bday
            candles_left = candles
print()                        # Creates a clear row to make output look better
print(f"Total number of boxes: {boxes}, Remaining candles: {candles_left}")
