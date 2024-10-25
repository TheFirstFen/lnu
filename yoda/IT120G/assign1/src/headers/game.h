#ifndef GAME_H
#define GAME_H

#include <iostream>
#include <vector>
#include <string>

bool oldEnough();
void printRules();
void gameHistory(std::vector<int> payout, std::vector<int> rounds, int vectorLength);
bool doYouWantTo(std::string question);
int game(int accountAmount, int totalWinAmount);
#endif
