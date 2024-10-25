#include <iostream>
#include "game.h"
#include "constants.h"

// The main entry point of the MatrixBandit program.
// Initializes the game, manages the main game loop, 
// processes user bets and total funds, and determines win or loss outcomes. 
// The game loop continues until the player chooses to stop or runs out of money.
int main() {

    std::cout << "Welcome to the one-armed bandit game!" << std::endl;
    int balance = 0;
    bool playGame = true;

    while (playGame) 
    {
        printBalance(balance);
        if (balance == 0)
        {
            balance = insertMoney();
		}
        int bet = getBetAmount(balance);
        balance -= bet;

        char gameField[fieldSize][fieldSize];
        generateSlotSymbols(gameField);
        displayGameField(gameField);

        int payout = determinePayout(gameField, bet);
        balance += payout;
        displayPayout(payout);

        playGame = playAgain();
    } 

    std::cout << "Thanks for playing! Your final balance is " << balance << " kr." << std::endl;
    return 0;
}