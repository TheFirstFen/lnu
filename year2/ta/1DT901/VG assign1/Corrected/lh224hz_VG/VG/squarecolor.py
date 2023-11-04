#Take user input
user = input("Enter a chess square identifier (e.g. e5): ")

#Split the starters by color
black_starter = ["a","c","e","g"]
white_starter = ["b","d","f","h"]

#Identify the starter (a letter) by spliting the input l and n (l = letter),(n = number)
if user[0] in black_starter:
    if int(user[1]) %2 == 0:
        color = "white"
    else:
        color = "black"

if user[0] in white_starter:
    if int(user[1]) %2 == 0:
        color = "white"
    else:
        color = "black"

print("The color of",user,color)


