#ifndef GAMEHISTORY_H
#define GAMEHISTORY_H

// modules
#include "boardFunctions.h"
#include "consts.h"
#include "mylibs.h"
#include "helpers.h"

// function declaration
void printWinLoss(std::vector<int> moneyWon, int size);
void printBoardHistory(std::vector<std::vector<std::vector<char>>>& historyBoards, int size);
std::vector<std::vector<char>> pointerToVector(char** board);


#endif