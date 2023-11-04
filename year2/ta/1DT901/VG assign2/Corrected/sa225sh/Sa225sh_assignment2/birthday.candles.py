def candles_calc():
    boxes = 0
    candles = 0
    for years in range(1, 101):
        yearly_boxes = 0
        while (years > candles):
            candles += 24
            yearly_boxes += 1

        candles -= years
        boxes += yearly_boxes
        print("Year", years, "Buy: ", yearly_boxes)

    print("Total boxes was", boxes, "remaining candles:", candles)


candles_calc()
