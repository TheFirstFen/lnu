#include "../headers/gameManager.h"

// function to manage the game logic
bool game() {
    int bank = newBankAmount();  // new bank deposit

    // vector to store the history of game boards
    std::vector<std::vector<std::vector<char>>> historyBoards;

    // vector to store the history of money won or lost in each round
    std::vector<int> historyMoney;

    int roundNumber = 0;  // tracks the current round number

    // continue the game while the player has money in the bank
    while (bank > 0) {
        // allocate memory for the game board
        std::cout << "Current amount in the bank " << bank << std::endl;
        char** board = gameBoard();

        int totalWinningAmount = gameRound(bank, board);
        bank += totalWinningAmount;

        // Store the current board and winnings in history
        historyBoards.push_back(pointerToVector(board));
        historyMoney.push_back(totalWinningAmount);
        roundNumber++;

        // Deallocate the memory used for the game board
        if (board != nullptr) {
            for (int i = 0; i < gameBoardSize; i++) {
                delete[] board[i];
            }
            delete[] board;
        }

        // ask the player if they want to see the round history
        if (again("Do you want to see the round history ")) {
            printWinLoss(historyMoney, roundNumber);
        }

        // ask the player if they want to see the board history
        if (again("Do you want to see the board history ")) {
            printBoardHistory(historyBoards, roundNumber);
        }

        // prompt the player to play another round
        if (!again("Do you want to play another round ")) {
            break;
        }
    }

    if (bank <= 0) {
        std::cout << "Your bank account is empty. ";
    }

    // ask the player if they want to restart the game
    return again("Do you want to restart the game ");
}
