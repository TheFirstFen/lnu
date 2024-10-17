#include "utils.h"
#include "constants.h"

#include <iostream>
#include <string>
#include <set>
#include <limits>

// Prompts the player about what input is expected, takes an integer input from the player, validates it and returns it
int getInputInt(std::string prompt)
{
	int enteredNumber;
	bool isValidInput = false;

	while (!isValidInput)
	{
		std::cout << prompt;
		std::cin >> enteredNumber;

		if (std::cin.fail())		// checks for fail flags in the input, for example if the value the player provided is not parsable to an integer.
		{
			std::cin.clear();		// clears the flags
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');	// discards the input buffer to make room for future validations
			std::cout << "Please enter a valid number." << std::endl;
		}
		else
		{
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			isValidInput = true;
		}
	}
	return enteredNumber;
}

// Prompts the player about what input is expected, takes a string input from the player and returns it
std::string getInputString(std::string prompt)
{
	std::string enteredString;

	std::cout << prompt;
	std::getline(std::cin, enteredString);	// sets the second argument to the value of the first input argument

	return enteredString;
}

// Checks if a number is zero or less
bool isZeroOrLess(int number)
{
	return number <= 0;
}

// Checks if the bet amount is among the amounts that are allowed according to the set of allowed bet amounts
bool isAllowedBetAmount(int bet) {
	return allowedBetAmounts.find(bet) != allowedBetAmounts.end();
}

// Prompts the player for a binary answer as a char (y/n), validates and returns it as a boolean
bool getAffirmation(std::string prompt)
{
	char binaryChar;
	bool isValidInput = false;

	while (!isValidInput)
	{
		std::cout << prompt << std::endl;
		std::cin >> binaryChar;

		if (binaryChar == 'y' || binaryChar == 'n')
		{
			isValidInput = true;
		}
		else
		{
			std::cout << "Not a valid choice. Please try again." << std::endl;
		}
	}
	return binaryChar == 'y';
}