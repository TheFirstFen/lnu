# Here's the function to buy candles. Note that i have 4 variables in and 3
# out. Age doesn't matter but i have 2 variables that keep track of candles
# and one that keeps track of boxes. Then one that helps the print for
# amount of boxes that were needed before the birthday.
def buy_candles(age, current_candles, boxes_baught, needed_boxes):

    # while loop to keep buying boxes until we have enough candles.
    while age > current_candles:
        current_candles += 24
        boxes_baught += 1
        needed_boxes += 1

    # return final values after purchase
    return current_candles, boxes_baught, needed_boxes


# cc = current candles, bb = boxes baught and nb = needed boxes.
cc = 0
bb = 0
nb = 0

# a for range that represents the age, 1 to 100.
for age in range(101):

    # call the function to calculate how many boxes we need to buy
    cc, bb, nb = buy_candles(age, cc, bb, nb)

    # print the results, only if we baught boxes before the birthday.
    if nb != 0:
        print(f"Before birthday {age}, buy {nb} box(es)")

    # here i subtract the candles needed for the birthday and also resets
    # the needed boxes to 0.
    cc -= age
    nb = 0

# print total boxes baught and how many candles we have left.
print(f"Total number of boxes: {bb}, Remaining candles: {cc}")
