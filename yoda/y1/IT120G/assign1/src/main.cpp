#include <iostream>
#include <ctime>
#include "headers/game.h"

// start values
const int emptySpace = 30;
const int intialCash = 1000;
const int intialWinAmount = 0;

// starts and ends the game
int main() {
    // random seed
	srand(time(0));
	
	printRules();
	bool isOldEnough = oldEnough();
	bool newGame = true; // default value to start the game
	std::string question = "Do you want to restart the game ";
	
	// checks if pers
	if (isOldEnough){
		while (newGame){
			// makes empty rows to clear the screen
			for (int i = 0; i < emptySpace; i++){
				std::cout << "\n";
			}

			game(intialCash, intialWinAmount); // starts each game
			newGame = doYouWantTo(question);
		}
	} else {
		std::cout << "You must be 18 years old or older to play the game" << std::endl;
	}
	std::cout << "Byeeeee!" << std::endl;
    std::cout << std::endl;

	return 0;
}

