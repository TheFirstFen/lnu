# 15 print colour of chess square by checking square picker

square_picker = input("Enter a chess square picker (e.g. e5): ")  # Input

if (((square_picker[0] == "a" or square_picker[0] == "c" or square_picker[0] == "e" or square_picker[0] == "g") and int(square_picker[1]) % 2 != 0)) or ((square_picker[0] == "b" or square_picker[0] == "d" or square_picker[0] == "f" or square_picker[0] == "h") and int(square_picker[1]) % 2 == 0):
    print(square_picker+" is black")  # Output

else:
    print(square_picker+" is white")  # Output

# Done
