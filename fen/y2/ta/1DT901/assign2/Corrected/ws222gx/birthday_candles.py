total_boxes, candels, boxes_needed = 0, 0, 0
candles_per_box = 24

# Loop from age 1 to 100
for age in range(101):
    boxes_needed = 0
    # adds a box and 24 candles as long as age is greater than candles
    while age > candels:
        candels += candles_per_box
        boxes_needed += 1

    candels -= age
    total_boxes += boxes_needed

    # if the boxes_needed are greater than 0 it prints
    if boxes_needed > 0:
        print(f"Before birthday {age}, buy {boxes_needed} box(es)")

print(f"\nTotal number of boxes: {total_boxes}, Remaining candles" +
      ":", candels)
