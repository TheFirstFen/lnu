def birthday_candles():
    total_boxes = 0
    remaining_candles = 0

    for age in range(1, 101):
        remaining_candles += age  # Add candles from current year

        if remaining_candles >= 24:  # Check if enough candles for next year
            boxes_needed = remaining_candles // 24
            total_boxes += boxes_needed
            remaining_candles %= 24

            print(f"Before birthday {age}, buy {boxes_needed} box(es)")

    print("\nTotal number of boxes: " + str(total_boxes) +
          ", Remaining candles: " + str(remaining_candles))


birthday_candles()
