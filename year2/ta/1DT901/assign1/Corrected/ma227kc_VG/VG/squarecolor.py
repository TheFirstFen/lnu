#User choosing a tile
choice = (input("Enter a chess square identifier (e.g. e5): "))

#Excluding non-existing tiles
if (choice[0] != "a", "b", "c", "d","e","f","g","h") or int(8<choice[1]<1):
    print("Tile does not exist")

#Checking tile letter and number then displaying incase the tile is black
elif ((choice[0] == "a" or choice[0] == "c" or choice[0] == "e" or choice[0] == "g") and int(choice[1])%2!=0) or ((choice[0] == "b" or choice[0] == "d" or choice[0] == "f" or choice[0] == "h") and int(choice[1])%2==0): 
    print(choice + " is black")


#No other possibility than white tiles
else :
    print(choice + " is white")