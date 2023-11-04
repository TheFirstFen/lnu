# Variables
box = 0
boxes = 0
candle = 0
# Computing and displaying part of the results
for i in range(1, 101):
    box = 0
    while i > candle:
        candle += 24
        box += 1
    boxes += box
    candle -= i
    print("Before Birthday", i, "Buy", box, "Box(es)")

# Displaying the rest of the results
print("Total boxes needed:", boxes,
      "candle available after 100 birthdays:", candle)
