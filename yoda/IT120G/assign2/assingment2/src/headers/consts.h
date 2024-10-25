// constants that are the same throughout every file.
#ifndef CONSTANTS_H
#define CONSTANTS_H

inline constexpr int gameBoardSize = 3; 
inline constexpr int fullBoardRows = 8;
inline constexpr int lastIndexNumber = 2;
inline constexpr int allowedAmountsSize = 3;
inline constexpr int lines = 13;

inline const std::string possibilities[3] = {"OOO", "AAA", "XXX"};
inline const char symbols[3] = {'O', 'A', 'X'};
inline const int allowedAmounts[3] = {100, 300, 500};


#endif // CONSTANTS_H
