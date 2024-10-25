#ifndef BOARDFUNCTIONS_H
#define BOARDFUNCTIONS_H

#include "mylibs.h"
#include "consts.h"
#include "bettingFunctions.h"
#include "helpers.h"

char** gameBoard();
char randomChar();
void printBoard(char** pointerBoard, std::vector<std::vector<char > > historyBoard={});
void printLines();
int checkBoard(char** board);
int gameRound(int bank, char** board);

#endif // BOARDFUNCTIONS_H
