chess_position = input("Enter a chess square idenifier (e.g. e5): " )

# Extract the first character and convert it to lowercase
chess_character = chess_position[0].lower()
# Extract the second character (number) and determine if it's odd or even
chess_number = int(chess_position[1]) %2 # 0 for even, 1 for odd 

print(chess_position, "is ",end="")

# if a,c,e or g: nummer odd = black else white 
# check the color of the chess square
if chess_character == "a" or chess_character == "c" or chess_character == "e" or chess_character =="g": 
    if chess_number == 0: 
        print("White")
    else: 
        print("Black")
elif chess_character =="b" or chess_character == "d" or chess_character =="f" or chess_character =="h":
    if chess_number == 0: 
        print("Black")
    else:
        print("White")
else: 
    print("not in 8x8 chess position") 
