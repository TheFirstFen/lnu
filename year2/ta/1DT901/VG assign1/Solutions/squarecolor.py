# Color of a chess square

square = input("Enter a chess square identifier (e.g. e5) ")
row = int(square[1])
col = square[0]

if row % 2 == 0:  # Even rows
    if col == "a" or col == "c" or col == "e" or col == "g":
        print("The square is White")
    else:
        print("The square is Black")
else:  # Odd rows
    if col == "a" or col == "c" or col == "e" or col == "g":
        print("The square is Black")
    else:
        print("The square is White")
