#include "../headers/boardFunctions.h"


// creates a random char between in the chars of (O, A, X)
char randomChar(){
    return symbols[rand() % gameBoardSize];
}

// creates the game board
char** gameBoard() {
    char** board = new char*[gameBoardSize];
    for (int i = 0; i < gameBoardSize; i++) {
        board[i] = new char[gameBoardSize];
    }

    for (int i = 0; i < gameBoardSize; i++) {
        for (int j = 0; j < gameBoardSize; j++) {
            board[i][j] = randomChar();
        }
    }
    return board;
}

// prints dividing lines
void printLines(){
    for (int i = 0; i < lines; i++){
        std::cout << "-";
    }
    std::cout << std::endl;
}

// prints the board / boards depending on if the user seeks the history or just regular board
void printBoard(char** pointerBoard, std::vector<std::vector<char > > historyBoard){
    
    std::vector<std::vector<char>> board;
    // if historyBoard is empty than we want the gameBoard to print out
    board = (!historyBoard.empty()) ? historyBoard : pointerToVector(pointerBoard);

    // prints out the board
    for(int row = 0; row < gameBoardSize; row++){
        printLines();
        for(int col = 0; col < gameBoardSize; col++){
            std::cout << "| " << board[row][col] << " ";
            if (col == lastIndexNumber){
                std::cout << "|";
            }
        }
        std::cout << std::endl;
    }
    printLines();
}

// checks the board for how many lines are equal to each other
int checkBoard(char** board){
    int filledRows = 0;
    std::string row;
    
    // horizontal rows
    for(int i = 0; i < gameBoardSize; i++){
        row = std::string(1, board[i][0]) + board[i][1] + board[i][2];
        for (int j = 0; j < gameBoardSize; j++){
            if (row == possibilities[j]){
                filledRows ++;
                break; // only one possibility per row can happen thus break
            }
        }
       
    }

    // vertical rows
    for (int i = 0; i < gameBoardSize; i++){
        row = std::string(1, board[0][i]) + board[1][i] + board[2][i];
        for (int j = 0; j < gameBoardSize; j++){
            if (row == possibilities[j]){
                filledRows ++;
            }
        }
    }

    // creates 2 different strings that gets compared to the the possibilities 
    std::string leftRightDig = std::string(1, board[0][0]) + board[1][1] + board[2][2];
    std::string rightLeftDig = std::string(1, board[0][2]) + board[1][1] + board[2][0];
    
    // diagonal rows
    for (int i = 0; i < gameBoardSize; i++){
        if (leftRightDig == possibilities[i]){
            filledRows ++;
        }

        if (rightLeftDig == possibilities[i]){
            filledRows ++;
        }
    }
    return filledRows;

}

// handles each gameRound
int gameRound(int bank, char** board){

    int bet = newBet(bank);
    bank -= bet;
    int totalWinningAmount;
    printBoard(board);
    // printBoard(board);
    std::cout << "Checking board for winning rows..." << std::endl;
    int filledRows = checkBoard(board);

    std::cout << "Calculating winning amount..." << std::endl;
    int winningAmount = payout(filledRows, bet);
    
    // Adjust bank amount based on the result
    if (winningAmount > 0) {
        std::cout << "You won " << winningAmount << " there were a total of ";
        std::cout << filledRows << " row(s)" << std::endl;
        totalWinningAmount = winningAmount + bet;
    } else {
        std::cout << "You lost" << std::endl;
        totalWinningAmount = -bet;
    }
    return totalWinningAmount;
}