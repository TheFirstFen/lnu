#include "constants.h"
#include "game.h"
#include "utils.h"

#include <cstdlib>
#include <ctime>
#include <iostream>

// Prints the player's current balance
void printBalance(int balance)
{
    std::cout << "Your current balance is " << balance << " kr." << std::endl;
}

// Prompts the player to insert money into the machine
int insertMoney() 
{
    int insertedAmount = 0;
    bool isValidInput = false;

    while (!isValidInput)
    {
        std::cout << "You can insert 100, 300 or 500 kr into the machine." << std::endl;
        insertedAmount = getInputInt("How much money do you want to insert? ");
        if (isAllowedBetAmount(insertedAmount))
		{
            std::cout << "You have chosen to insert " << insertedAmount << " kr." << std::endl;
			isValidInput = true;
		}
		else
		{
			std::cout << "Not a valid amount. Please try again." << std::endl;
		}
	}
    return insertedAmount;
}

// Gets and validates the bet amount as an input from the player, checking it does not exceed the balance
int getBetAmount(int balance)
{
    int bet = 0;
    bool isValidInput = false;

    while (!isValidInput)
    {
        std::cout << "How much do you want to bet for this spin?" << std::endl;
        bet = getInputInt("Please enter you bet amount: ");

        if (isZeroOrLess(bet))
        {
            std::cout << "You have to bet to play." << std::endl;
            std::cout << "Please adjust your bet." << std::endl;
        }
        else if (bet > balance)
        {
            std::cout << "You cannot afford this bet!" << std::endl;
            std::cout << "Please adjust your bet." << std::endl;
        }
        else
        {
            std::cout << "You have chosen to bet " << bet << " kr." << std::endl;
            isValidInput = true;
        }
    }
    return bet;
}

// Generates random symbols for each position or slot in the game field
void generateSlotSymbols(char gameField[fieldSize][fieldSize]) // gameField passed as ref parameter
{
    srand(time(0));
    for (int i = 0; i < fieldSize; ++i)
    {
        for (int j = 0; j < fieldSize; ++j)
        {
            gameField[i][j] = slotSymbols[rand() % 3];
        }
    }
}

// Displays the current game field to the player
void displayGameField(const char gameField[fieldSize][fieldSize])
{
    std::cout << "Pulling lever-arm and spinning slots..." << std::endl;
    for (int i = 0; i < fieldSize; ++i)
    {
        for (int j = 0; j < fieldSize; ++j)
        {
            std::cout << gameField[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

// Calculates the number of matching lines and returns the corresponding payout calculated from the bet
int determinePayout(const char gameField[fieldSize][fieldSize], int bet)
{
    int matchingLines = 0;
    for (int i = 0; i < fieldSize; ++i)
    {
        if (gameField[i][0] == gameField[i][1] && gameField[i][0] == gameField[i][2]) 
        {
            matchingLines++;
        }
        if (gameField[0][i] == gameField[1][i] && gameField[0][i] == gameField[2][i]) 
        {
            matchingLines++;
        }
    }
    if (gameField[0][0] == gameField[1][1] && gameField[0][0] == gameField[2][2]) 
    {
        matchingLines++;
    }
    if (gameField[0][2] == gameField[1][1] && gameField[0][2] == gameField[2][0]) 
    {
        matchingLines++;
    }

    switch (matchingLines) {
    case 1: return bet * 2;
    case 2: return bet * 3;
    case 3: return bet * 4;
    case 4: return bet * 5;
    case 5: return bet * 7;
    case 6: return bet * 10;
    default: return 0;
    }
}

// Displays the calculated payout to the player
void displayPayout(int payout) 
{
    if (payout > 0) {
        std::cout << "Congratulations, you won " << payout << " kr!" << std::endl;
    }
    else {
        std::cout << "No luck this time, try again!" << std::endl;
    }
}

// Asks the player if they want to play again
bool playAgain() 
{
    return getAffirmation("Do you want to play again? (y/n) ");
}
