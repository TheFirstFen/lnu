chess_square = input("Enter a chess square identifier (e.g. e5): ").lower()

# grouping the starter colorstogether
black_starters = ("a", "c", "e", "g")
white_starters = ("b", "d", "f", "h")

# checks if the first character is in the black_starters tuple
if (chess_square[0] in black_starters):
    # check if the second character is in even/odd to determine color of square
    if (int(chess_square[1]) % 2 == 0):
        print(chess_square, "is White")
    else:
        print(chess_square, "is Black")

# check if the first character is in the white_starters tuple
elif (chess_square[0] in white_starters):
    if (int(chess_square[1]) % 2 == 0):
        print(chess_square, "is Black")
    else:
        print(chess_square, "is White")
