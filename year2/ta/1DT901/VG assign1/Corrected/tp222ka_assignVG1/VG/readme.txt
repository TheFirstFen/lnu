Files submitted: 
    change.py
    squarecolor.py 
    sumofthree.py
    taxes.py

VG sum of three: 

read 3 digit into input as int 
use (//) floor division to get the first number 
then i use moduls % 100 then use // to get the second number 
the last number just use %10. 

then store the value of the number in new variabel and print it using f-string 

VG change: 

taking input from the keybord and store it in variabel. price / payment 
then calculates the quantity of each bill or coin in the change using 
floor division (//) and the modulo operator (%). begining with the largest bills (1000kr)
and works its way down to the smallest coins (1kr), updating the change variable each time how many bills/ coins it can fit. 


VG taxes: 

calculates taxes rate based on income using "if" "elif" "else".
if income is between 0 and 38,000kr. income* 0.3 

if income is between 38,001kr and 50,000kr. 
35% tax on income above 38,000kr.
30% tax on income up to 38,000kr.
add the two sum together = total money after taxes 

if income is above 50,000kr,
35% tax on income above 38,000kr and up to 50,000kr.
30% tax on income up to 38,000kr.
40% tax on income above 50,000kr.
add the three sum together = total money after taxes 



VG: squarecolor 


take out the first character from the input and converts it to lowercase 
in case the user type in uppercase character. The character is the column of the chessboard. 

the second character is a number, converted it into integer and checked if its odd or even 
using modulo operator(%). if it's even, chess_number is set to 0; otherwise, it's set to 1.

The code then check the color of the chess square based on the column (letter) and whether the row 
(number) is odd or even. the chessboards have an alternating black and white squares. 

 
