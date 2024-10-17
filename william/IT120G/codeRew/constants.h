#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <set>

inline constexpr int fieldSize = 3;

inline constexpr char slotSymbols[] = { 'A', 'O', 'X' };

extern const std::set<int> allowedBetAmounts;

#endif