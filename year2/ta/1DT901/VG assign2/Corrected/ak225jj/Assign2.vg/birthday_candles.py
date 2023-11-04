
total_boxes = 0
candles = 0

for i in range(1, 101):
    open_box = 0
    while candles < i:
        candles += 24
        open_box += 1
    candles -= i
    total_boxes += open_box
    if open_box > 0:
        print(f"Before birthday {i}, buy {open_box} box(es)")

print()
print(f"Total number of boxes: {total_boxes}, Remaining candles: {candles}")
