#ifndef bettingFunction_H
#define bettingFunction_H

#include <iostream>


int getUserColor();
int colorOption(int bet, char wheelColor);
int getUserNumber();
int numberOption(int bet, int wheelNum);
bool checkNumWin(int numberChoice, int wheelResult);
bool checkColorWin(int wheelResult, char color);

#endif