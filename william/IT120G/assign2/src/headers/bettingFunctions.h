#ifndef BETTINGFUNCTIONS_H
#define BETTINGFUNCTIONS_H

#include "mylibs.h"
#include "consts.h"

int payout(int matchingLines, int bet);
int newBet(int accountAmount);
int newBankAmount();
bool depositAmountAllowed(int bet);

#endif