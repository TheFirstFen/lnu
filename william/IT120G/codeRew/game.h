#ifndef GAME_H
#define GAME_H

#include "constants.h"

// Prints the player's current balance
void printBalance(int balance);

// Prompts the player to insert money into the machine
int insertMoney();

// Gets and validates the bet amount as an input from the player, checking it does not exceed the balance
int getBetAmount(int balance);

// Generates random symbols for each position or slot in the game field
void generateSlotSymbols(char gameField[fieldSize][fieldSize]);

// Displays the current game field to the player
void displayGameField(const char gameField[fieldSize][fieldSize]);

// Calculates the number of matching lines and returns the corresponding payout calculated from the bet
int determinePayout(const char gameField[fieldSize][fieldSize], int bet);

// Displays the calculated payout to the player
void displayPayout(int payout);

// Asks the player if they want to play again
bool playAgain();

#endif