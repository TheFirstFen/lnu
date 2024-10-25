#include "../headers/helpers.h"

bool again(std::string question){
    char anotherRound;
    std::cout << question <<" (Y/N)? ";
    std::cin >> anotherRound;
    std::cout << std::endl;

    anotherRound = toupper(anotherRound);
    
    // input validation
    while(anotherRound != 'Y' && anotherRound != 'N'){
        std::cout << "Unknown choice try again: ";
        std::cin >> anotherRound;
        std::cout << std::endl;
    }

    return (anotherRound == 'Y') ? true: false;
}

void printRules(){
    std::cout << "\t\t\tWelcome to the One-Armed Bandit Game!" << std::endl;
    std::cout << "Rules:" << std::endl;
    std::cout << "1. You can start by inserting money, choosing one of the amounts: 100kr, 300kr, or 500kr." << std::endl;
    std::cout << "2. For each game, you place a bet from your available money." << std::endl;
    std::cout << "3. The game generates a 3x3 grid with random symbols." << std::endl;
    std::cout << "4. The goal is to match as many rows, columns, and diagonals of the same symbol as possible." << std::endl;
    std::cout << "5. The payout is based on the number of matching rows, columns, and diagonals:" << std::endl;
    std::cout << "\n\t- One matching line: 2 * bet" << std::endl;
    std::cout << "\t- Two matching lines: 3 * bet" << std::endl;
    std::cout << "\t- Three matching lines: 4 * bet" << std::endl;
    std::cout << "\t- Four matching lines: 5 * bet" << std::endl;
    std::cout << "\t- Five matching lines: 7 * bet" << std::endl;
    std::cout << "\t- Full grid with the same symbol: 10 * bet" << std::endl;
}

void clear(){
    const int clearing = 40;
    for (int i = 0; i < clearing; i++){
        std::cout << "\n";
    }
}

// makes a pointer array into a vector
std::vector<std::vector<char>> pointerToVector(char** board){
    std::vector<std::vector<char>> tempBoard(gameBoardSize, std::vector<char>(gameBoardSize));

    for(int row = 0; row < gameBoardSize; row++){
        for(int col = 0; col < gameBoardSize; col++){
            tempBoard[row][col] = board[row][col];
        }
    }
    return tempBoard;
}