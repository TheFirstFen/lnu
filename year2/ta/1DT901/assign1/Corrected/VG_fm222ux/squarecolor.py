# Read input
square = input("Enter a chess square identifier (e.g. e5): ")

# Conditions and result
if square[0] == "a" or square[0] == "c" or square[0] == "e" or square[0] == "g":
    if int(square[1]) % 2 == 0:
        print(f"\n{square} is White")

    elif int(square[1]) % 2 == 1:
        print(f"\n{square} is Black")

elif square[0] == "b" or square[0] == "d" or square[0] == "f" or square[0] == "h":
    if int(square[1]) % 2 == 0:
        print(f"\n{square} is Black")
    
    elif int(square[1]) % 2 == 1:
        print(f"\n{square} is White")
  


        
