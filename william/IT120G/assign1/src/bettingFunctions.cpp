#include <iostream>

const int lowBound = 1;
const int highBound = 36;

// checks if the chosen number is equal to wheel result
bool checkNumWin(int numberChoice, int wheelResult){
	return numberChoice == wheelResult;
}

// checks if the chosen color is equal to wheel result
bool checkColorWin(int wheelResult, char color){
	return color == wheelResult;
}

// asks for the user to provide the color 
int getUserColor(){
	char color;
	std::cout << "\nChoose either black(S) or red(R): ";
	std::cin >> color;

	while (toupper(color) != 'S' && toupper(color) != 'R'){
		std::cout << "\nInvalid color, try again: ";
		std::cin >> color;
	}

	return toupper(color);
}

// Handles color option if player have done its bet on color
int colorOption(int bet, char wheelColor){
    char color = getUserColor();
    
    if (checkColorWin(wheelColor, color)){
      std::cout << "WIN!!! your bet increased by 2 times\n";
      return bet*2;

	}
	std::cout << "Lose sorry. ";
    return 0;
}

// Asks user for its guess on a number
int getUserNumber(){

  	int number;

  	std::cout << "Pick a number between 1 and 36: ";
  	std::cin >> number;

	// checks if the number is a valid type & that it is in the bounds of the game
	while (std::cin.fail() || number < lowBound || number > highBound){
		std::cin.clear();
		std::cin.ignore();

		std::cout << "\nInvalid number, it must be in between 1 and 36, ";
		std::cout << "try again: ";
		std::cin >> number;
	}
	return number;
}

// Handles if the user chooses to bet on a number
int numberOption(int bet, int wheelNum){
	int number = getUserNumber();
	int amountChange = 0;

	if (checkNumWin(number, wheelNum)){
		std::cout << "\nWIN!!! your bet has increased by 10 times\n";
		return bet * 10;
	}
	// base case
	std::cout << "Lose sorry. ";
	return 0;
}