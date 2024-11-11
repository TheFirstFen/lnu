# Function that prints the board
def board(r0, r1, r2, r3):
    for i in r0:
        print(i, end=" ")
    print()
    for i in r1:
        print(i, end=" ")
    print()
    for i in r2:
        print(i, end=" ")
    print()
    for i in r3:
        print(i, end=" ")
    print()


# Function that places the players sign on the desired position
def place(round, r, c, r1, r2, r3):
    if r == 1:           # For each row value select the correct list
        r = r1
        temp = r1        # Store a temp value to remember the list to alter
    elif r == 2:
        r = r2
        temp = r2
    elif r == 3:
        r = r3
        temp = r3
    if round % 2 == 0:  # Checks whose turn it is
        r[c] = "X"      # Replaces the correct position by the correct sign
    else:
        r[c] = "O"
    if temp == r1:      # Checks the remembered list to alter
        r1 = r          # Replaces the row list with the altered list
        return r1       # Returns the new altered but corrct list
    elif temp == r2:
        r2 = r
        return r2
    elif temp == r3:
        r3 = r
        return r3


# Returns True if X has won and False if not by checking all possible ways
def check_x_win(r1, r2, r3):
    if r1 == [1, "X", "X", "X"] or r2 == [2, "X", "X", "X"] \
       or r3 == [1, "X", "X", "X"]:
        return True
    elif r1[1] == "X" and r2[1] == "X" and r3[1] == "X":
        return True
    elif r1[2] == "X" and r2[2] == "X" and r3[2] == "X":
        return True
    elif r1[3] == "X" and r2[3] == "X" and r3[3] == "X":
        return True
    elif r1[1] == "X" and r2[2] == "X" and r3[3] == "X":
        return True
    elif r1[3] == "X" and r2[2] == "X" and r3[1] == "X":
        return True
    else:
        return False


# Returns true if O has won and False if not by checking all possible ways
def check_o_win(r1, r2, r3):
    if r1 == [1, "O", "O", "O"] or r2 == [1, "O", "O", "O"] \
            or r3 == [1, "O", "O", "O"]:
        return True
    elif r1[1] == "O" and r2[1] == "O" and r3[1] == "O":
        return True
    elif r1[2] == "O" and r2[2] == "O" and r3[2] == "O":
        return True
    elif r1[3] == "O" and r2[3] == "O" and r3[3] == "O":
        return True
    elif r1[1] == "O" and r2[2] == "O" and r3[3] == "O":
        return True
    elif r1[3] == "O" and r2[2] == "O" and r3[1] == "O":
        return True
    else:
        return False


# Checks if the users desired position is taken or not
def is_taken(r, c, r1, r2, r3):
    if r == 1:
        r = r1
    elif r == 2:
        r = r2
    elif r == 3:
        r = r3
    if r[c] == "-":     # If position contains - its free and thus returns True
        return True
    else:
        return False


# Asks the user to input the desired position and returns its row and column
def player_input(round):
    if round % 2 == 0:          # Checks whose turn it is
        column = int(input("Player X, which column do you play? "))
        row = int(input("Player X, which row do you play? "))
        return row, column
    else:
        column = int(input("Player O, which column do you play? "))
        row = int(input("Player O, which row do you play? "))
        return row, column


# Returns true if the desired position is on the board
def in_board(r, c):
    return 1 <= r <= 3 and 1 <= c <= 3


# Funtion that checks if X or O has won or if its a draw
def check_if_end(round, r1, r2, r3):
    if check_x_win(r1, r2, r3):
        print("X Wins!!")   # Prints if X has won
        return True         # Returns True if X has won to end the game
    elif check_o_win(r1, r2, r3):
        print("O wins!!")   # Prints if O has won
        return True         # Returns True if O has won to end the game
    elif round == 10:       # If True its a draw eacuse the board is full
        print("Draw!!")     # Prints if its a draw
        return True
    else:                   # If its not finished return false to continue game
        return False


# Creates the board containing a list for each row
r0 = [" ", 1, 2, 3]
r1 = [1, "-", "-", "-"]
r2 = [2, "-", "-", "-"]
r3 = [3, "-", "-", "-"]

board(r0, r1, r2, r3)       # Prints the starting board

round = 1                   # Sets the round to 1 to start the game

# While loop keeps the game going until check_if_win is True
while check_if_end(round, r1, r2, r3) is False:
    row, column = player_input(round)       # Stores the desired row and column
    while in_board(row, column) is False:
        # Asks the user for a new input if its not on the board
        print("Please provide a spot on the board...!")
        row, column = player_input(round)
    while is_taken(row, column, r1, r2, r3) is False:
        # Asks the user for a new input if the position is already taken
        print("Already taken!")
        row, column = player_input(round)
    place(round, row, column, r1, r2, r3)   # Places sign on desired position
    board(r0, r1, r2, r3)                   # Prints the updated board
    round += 1                              # Starts a new round
