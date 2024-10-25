#include "../headers/gameHistory.h"

// prints money won / lost per game round
void printWinLoss(std::vector<int> moneyWon, int size){
    for (int roundNumber = 0; roundNumber < size; roundNumber++){
        std::cout << "Round number: " << roundNumber+1 << " Money won/loss " << moneyWon[roundNumber] << std::endl;
    }
}

// prints each board for each round using the printBoard function
void printBoardHistory(std::vector<std::vector<std::vector<char>>>& historyBoards, int size) {
    for (int roundNumber = 0; roundNumber < size; ++roundNumber) { // Iterate from 0 to size-1
        std::vector<std::vector<char>> board = historyBoards[roundNumber];
        printBoard(NULL, board); // Assuming printBoard accepts a vector of vector of char
        std::cout << "\n\n";
    }
}