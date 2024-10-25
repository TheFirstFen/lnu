#ifndef UTILS_H
#define UTILS_H

#include <string>

// Prompts the player about what input is expected, takes an integer input from the player, validates it and returns it
int getInputInt(std::string prompt);

// Prompts the player about what input is expected, takes a string input from the player and returns it
std::string getInputString(std::string prompt);

// Checks if a number is zero or less
bool isZeroOrLess(int number);

// Checks if the bet amount is among the amounts that are allowed according to the set of allowed bet amounts
bool isAllowedBetAmount(int bet);

// Prompts the player for a binary answer as a char (y/n), validates and returns it as a boolean
bool getAffirmation(std::string prompt);

#endif