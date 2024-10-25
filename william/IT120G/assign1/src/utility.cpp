#include "headers/utility.h"
#include <iostream>
#include "headers/bettingFunctions.h"


const int bet100 = 100;
const int bet300 = 300;
const int bet500 = 500;

// asks for if you want to bet on number or color
char betType(){
	char typeChoice;

	std::cout << "\nNumber(N) or color(C)? ";
	std::cin >> typeChoice;
	
	while(toupper(typeChoice) != 'N' && toupper(typeChoice) != 'C'){
		std::cout << "\nInvalid choice, it has to be either (N/C), try again: ";
		std::cin >> typeChoice;
	}
	std::cout << std::endl;
	return typeChoice;
}

// Simulates wheel spin, a random number will be generated from 1-36
	int wheelSpin(){
	return rand() % 1 + 1;
	}

// checks if the bet is not the correct currency (100, 300, 500)
bool isBetCorrectValue(int bet){
	return bet != bet100 && bet != bet300 && bet != bet500;
}

// Asks the user for a bet amount
int betAmount(int accountAmount){
	int bet;
	
	std::cout << "\n\nAccount: " << accountAmount << "$" << std::endl;
	
	std::cout << "How much do you want to bet\n";
	std::cout << "You can bet these amounts, 100$, 300$, 500$: ";
	std::cin >> bet;
	
	// loop to validate the bet amount
	while (std::cin.fail() || bet > accountAmount || isBetCorrectValue(bet)) {
		std::cin.clear(); // clears errors on cin
		std::cin.ignore(); // ignores the last cin output basically removing the value from bet
		std::cout << "\nYou cannot bet this amount\n";

		// checks to see if the bet exceeds the account amount
		if (bet > accountAmount){
			std::cout << "You have insufficent funds try again with a smaller value: ";
		} else {
			std::cout << "You must pick one of these amounts 100$, 300$, 500$ try again: ";
		}
		
		std::cin >> bet;
	}
	
	std::cout << std::endl;
	std::cout << bet << "$ have been taken out of your account...\n ";

	return bet;
}

// detiermens the outcome of the game, depending on user's choice and bet amount
int gameTable(char choice, int bet){
	int randNum = wheelSpin();
	char wheelColor = (randNum % 2 == 0) ? 'S': 'R'; // Even numbers are black and odds are red
  
	int amountToChange = 0;
	amountToChange = (choice == 'N') ? numberOption(bet, randNum): colorOption(bet, wheelColor);

	std::cout << "The wheel landed on: " << randNum << " where the color is ";
	if (wheelColor == 'S'){
		std::cout << "black" << std::endl;
	} else {
		std::cout << "red" << std::endl;
	}

	return amountToChange;
}