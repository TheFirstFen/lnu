candles = 0
boxes = 0
for i in range(1, 101):
    yearly_boxes = 0
    #  adds boxes until there is enough
    while (i > candles):
        candles += 24
        yearly_boxes += 1
    #  subtracts the age from candles
    candles -= i

    #  adds to total boxes
    boxes += yearly_boxes
    if (yearly_boxes > 0):
        print("Before birthday", i, ", buy", yearly_boxes, "box(es)")

print("Total number of boxes: ", boxes, ", Remaining candles: ", candles)
