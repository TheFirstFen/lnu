#reads a string from user and converts it to lower case
answer = input("Please enter a chess square (e.g. a3): ").lower()

#checks the first character using if-statements and then moving on to the second characters, then printing the resulting color of the square.
if(answer[0] == "a","c","e","g"):
    if(answer[1] == "1" , "3" , "5" , "7"):
        print(answer, "is black")
    elif(answer[1] == "2" , "4" , "6" , "8"):
        print(answer, "is white")
    else:
        print("The provided chess square is not a chess square.")
elif (answer[0] == "b" , "d" , "f", "h"):
    if(answer[1] == "1" , "3" , "5" , "7"):
        print(answer, "is white")
    elif(answer[1] == "2" , "4" , "6" , "8"):
        print(answer, "is black")
    
    #If the given answer is not a chessquare, it prints out an error message.
    else:
        print("The provided chess square is not a chess square.")