# tic_tac_toe.py
#
# Author: Samuel Berg
# Date: 14-Sep-2022

''' winner function:
Checks all the different ways to win and returns True if one of them are met
otherwise returns False
'''


def winner(b):
    for i in range(len(b)):
        if (check_for_win(b[0][i], b[1][i], b[2][i]) or
                check_for_win(b[i][0], b[i][1], b[i][2])):
            return True
        elif (check_for_win(b[0][0], b[1][1], b[2][2]) or
                check_for_win(b[0][2], b[1][1], b[2][0])):
            return True
    return False


''' check_for_win function:
Checks if any of the given values are None and if even one is returns False
otherwise checks if all given values are equal if not returns False if they
are returns True
'''


def check_for_win(x, y, z):
    if x is None or y is None or z is None:
        return False
    else:
        return x == y == z


def display_board(board):
    print('  1 2 3')
    for i, row in enumerate(board):
        print(i + 1, get_attribute(row[0]), get_attribute(
            row[1]), get_attribute(row[2]))
    return board


'''get_row_col function:
Is called when there is wrong input given an player needs to reenter
coordinates or player selected already played coordinates
'''


def get_row_col():
    # Gets the row and column input of the user of where to place there symbol
    row = int(
        input(f'Player {get_attribute(turn)}, which row do you play? '))
    col = int(
        input(f'Player {get_attribute(turn)}, which column do you play? '))
    # Makes the move with the input
    move(board, col, row, turn)


''' get_attribute function:
Checks what the different "squares" on the board have for symbol or
if they are blank and returns the corresponding symbol as a string
'''


def get_attribute(b):
    if b is None:
        return '-'
    elif b is False:
        return 'X'
    else:
        return 'O'


''' move function:
Places the current players symbol on the given coordinates and if there already
exists a symbol at the given position request new input
'''


def move(board, col, row, turn):
    if row > 3 or col > 3:
        print('Select an actual spot on the board.')
        get_row_col()
    elif row < 1 or col < 1:
        print('Select an actual spot on the board.')
        get_row_col()
    elif board[row - 1][col - 1] is None:
        board[row - 1][col - 1] = turn
    else:
        print('Select an empty spot on the board.')
        get_row_col()


'''
Board:
  1 2 3
1 - - -
2 - - -
3 - - -
None = -
False = X
True = O
'''
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]]

# Keeps track of whose turn it is
turn = False
turn_counter = 0

# Actual game loop
while True:
    # Displays the current board
    display_board(board)

    # Asks for row and column player wants to put their symbol
    get_row_col()

    # Checks if there is a winning combination on the board
    if winner(board):
        display_board(board)
        print(f'Player {get_attribute(turn)} won!')
        exit()
    elif turn_counter == 8:
        print('Draw!')
        exit()
    turn = not turn  # Changes whose turn it is
    turn_counter += 1
