#include "headers/game.h"
#include "headers/utility.h"
#include <iostream>
#include <vector>
#include <string>

const int minAge = 18;
const int lineLength = 100;

// checks if the person playing is old enough 
bool oldEnough(){
	int age;
	std::cout << "\nType your age: ";
    std::cin >> age;
	while (std::cin.fail()) {
		std::cin.clear();
        std::cin.ignore();
        std::cout << "\nInvalid value, try again: ";
        std::cin >> age;
	}
	return age >= minAge;
}

// prints the rules of the game
void printRules(){
	std::cout << "Welcome to roulette the rules are the following:\n";
	
	std::cout << "1. You must be 18 years or older to play this game ";
	std::cout << "as this is a casino based game" << std::endl; 
	
	std::cout << "2. The game continues to run until you have no money left "; 
	std::cout << "or until you chose to end the game" << std::endl;
	
	std::cout << "3. By choosing the correct number your bet will increase by 2 times your bet & ";
	std::cout << "choosing number will increase it by 10 times your bet" << std::endl;
	
	std::cout << "4. Most important good luck and have fun\n";
}

// prints the gamehistory 
void gameHistory(std::vector<int> payout, std::vector<int> rounds, int vectorLength){
	
	std::cout << "\nHistory: " << std::endl;
	std::cout << "Round Nr\tResult" << std::endl;

	for (int i = 0; i < vectorLength; i++){
        std::cout << rounds[i] << "\t\t" << payout[i] << "$"<< std::endl; 
        }
}

// general function to make it easier for a choice question to get asked
bool doYouWantTo(std::string question){
	char choice;
    std::cout << question <<" (Y/N)? ";
    std::cin >> choice;

    while (toupper(choice)!= 'Y' && toupper(choice)!= 'N'){
        std::cout << "\nInvalid choice, you most chose (Y/N), try again: ";
        std::cin >> choice;
    }
    std::cout << std::endl;
    return (toupper(choice) == 'Y') ? true: false;
}

// simulets each game round
int game(int accountAmount, int totalWinAmount){
	int rounds = 1; 
	bool newRound = true;
	int winAmount;
	
	std::vector <int> historyPayOut;
	std::vector <int> historyRound;
		
	while (accountAmount > 0){
		
		int bet = betAmount(accountAmount);
		accountAmount -= bet; // remove bet from account

		char choice = betType(); // color or number
		winAmount = gameTable(toupper(choice), bet);

		
		// checks to see if it is a win or lose
		if (winAmount > 0){
			historyPayOut.push_back(winAmount);
			totalWinAmount += winAmount;
			// if win the bet should come back + the win amount
			accountAmount += winAmount + bet + bet;
		} else {
			historyPayOut.push_back(-bet);
			totalWinAmount -= bet;
		}

		if (rounds > 1){
			std::cout << "Round: " << rounds << "\tTotal money won/lost: " 
			<< totalWinAmount << "\n";
		}
		
		historyRound.push_back(rounds);
		
		rounds += 1;
		
		if(accountAmount <= 0){
			std::cout << "You have run out of cash and therefor cannot continue to play :(" << std::endl;
			break;
		}

		std::string question = "Another round ";
		bool newRound = doYouWantTo(question);

		if (!newRound){
			break;
		}	

		// makes it easier to see when a new round is happening
		for (int i =  0; i < lineLength; i++) {
			std::cout << "-";
		}
		std::cout << std::endl;
	}
		gameHistory(historyPayOut, historyRound, historyPayOut.size());
		return 0;
}
