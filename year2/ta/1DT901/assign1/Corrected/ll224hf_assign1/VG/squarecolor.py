#Enter a chess square identifier (e.g. e5): c6
#    
#    c6 is White


# First make up the chessboard, we have 2 different ways the squares can be layered;
# Ex 1st row (a) [BWBWBWBW] and 2nd row (b) [WBWBWBWB]
# So let's make 2 rows - BF = Black first and WF = White first. and then continue 
# alternating between the 2 every other number
BF = "BWBWBWBW"
WF = "WBWBWBWB"

# next id the rows to color formation                             a  B W B W B W B W
# i'll structure the board with the following structure in mind:  b  W B W B W B W B
#                                                                 c  B W B W B W B W
#                                                                 d  W B W B W B W B
#                                                                 e  B W B W B W B W
#                                                                 f  W B W B W B W B
#                                                                 g  B W B W B W B W
#                                                                 h  W B W B W B W B
#                                                                    1 2 3 4 5 6 7 8
# I think this will be easier to code, we'll see i guess :)

a = BF
b = WF
c = BF
d = WF
e = BF
f = WF
g = BF
h = WF

# There, we've now structured the board.
# Next we require the input so we can find the corosponding square. ALSO must make sure that input is a valid square i.e a to h AND 1 to 8.. ugh

text = input("Enter a chess square identifier (e.g. e5): ")
# first check if valid chess square
#first 1st char then 2nd char.
# Fetch the letter and make new variable for it.
letter = (text[0])
if (letter == "a" or letter == "b" or letter == "c" or letter == "d" or letter == "e" or letter == "f" or letter == "g" or letter == "h"):
    if letter == "a":
        letter = a
    elif letter == "b":
        letter = b
    elif letter == "c":
        letter = c
    elif letter == "d":
        letter = d
    elif letter == "e":
        letter = e
    elif letter == "f":
        letter = f
    elif letter == "g":
        letter = g
    else:
        letter = h

    # Fetch number and make a new variable for it, i think making it an integer now should make it easier.
    number = int(text[1])
    if (number > 0 and number < 9):

        #identify square
        square = (letter[number-1])
        
        if square == "W":
            print("The square is White!")
        else: #don't need to identify if square is "B" cause that's the only other option.
            print("The square is Black!")
    # If no valid number is provided, present the given "square" and say it's not valid.        
    else:
        print(text, "is not a valid square")
        
else:
    # If no valid letter is provided, present the given "square" and say it's not valid.
    print (text, "is not a valid square")