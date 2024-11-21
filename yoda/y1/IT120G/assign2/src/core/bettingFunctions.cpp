#include "../headers/bettingFunctions.h"

int payout(int matchingLines, int bet){
    switch (matchingLines){
    case 1: return bet*2;
    case 2: return bet*3;
    case 3: return bet*4;
    case 4: return bet*5;
    case 5: return bet*7;
    case 6: return bet*8;
    case fullBoardRows: return bet*10;
    default: return 0;
    }
}

// checks if the deposit is allowed in the given limits so (100, 300, 500)
bool depositAmountAllowed(int deposit){
    for(int i = 0; i < allowedAmountsSize; i++){
        if(deposit == allowedAmounts[i]){
            return true;
        }
    }
    return false;
}

// asks the user to bet 
int newBet(int accountAmount){
    int bet;
    std::cout << "How much do you want to bet for your game? ";
    std::cin >> bet;
    
    // input validation
    while (std::cin.fail() || bet > accountAmount){
        std::cin.clear();
        std::cin.ignore();

        if(bet > accountAmount){
            std::cout << "Insufficent funds ";
        } else {
            std::cout << "You cannot bet that ";
        }
        std::cout << "try again: ";
        std::cin >> bet;
    }
    return bet;
}

// creates a new deposit of money into the game
int newBankAmount(){
    int bank;
    std::cout << "How much money do you want to put in? ";
    std::cin >> bank;
    std::cout << std::endl;

    // input validation
    while(std::cin.fail() || !depositAmountAllowed(bank)){
        std::cin.clear();
        std::cin.ignore();

        std::cout << "You cannot put in that value try again: ";
        std::cin >> bank;
    }
    return bank;
}