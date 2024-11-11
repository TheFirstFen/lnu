Countdigits.py:

I solved countdigits by checking each of the integers in the number provided. First i defined a function that checks if it's even.
I then took the input from the user and created three variables, even, odd and zeros. I later created a for loop that check
for i in range of the number provided. To not miss checking the first number I check we check i - 1. I check that if its equal to zero
add one to zero variable and if its not zero call for the function is_even. if the function returns true add 1 to even and if its false
add 1 to odds. Then this repeats until all numbers are checked. After all integers have been checked it prints out the result.


birthday_candles.py:

To solve birthday candles i first defined all variables necessary. I had one for what birthday it is, one for current candles, one for
the amount of boxes bought, one for how many new boxes needed and one for how many candles that are left after 100th birthday.
I created a for loop that checked each birthday up to 100. In the for loop there is a while loop that keeps adding new boxes with candles
until there is enough. Then if there is enough candles it checks if there was a new box needed by checking the variable new_box.
If no new box was needed then it removes the birthday amount from candles variable. If new_box variabel is not equal to 0 after
a birthday then the program prints the current birthday and how many new boxes that needs to be bought. It then updates the new_box
variable to zero to prepare for the next birthday. It also updates the candles variable by removing all candles used. 
The program then outputs a blank line and the amount of boxes bought in total and how many candles left after 100th birthday.


abcd.py:

To solve abcd.py i first created a function that turns 4 separate numbers into one number and returns that number. I then created four 
variables that is the numbers to be generated. Then a nested for loop that keeps checking each possible numbers until the if statement
is true. These for loops uses different ranges for a and d because these can not be zero for the equation to work out.
The if statements then uses the get_number function to check if its true, and when a, b, c, d is such that it true it prints
the correct number by again using get_number function.


pi_approx.py:

When solving pi_approx i used the fact that if x ** 2 + y ** 2 is equal to one or less its either on the circle or in it.
I began by creating a variable that checks this and return true if it is in or on the circle. After that i created a main
function that checks for each provided number of points, n. First i created two variables one count to keep the amount of
points created correct and ins to keep track of how many of the points that are in the circle. Then a while loop that 
keeps going until the count of points created is equal to the n amount provided to check. It starts by creating a random
coordinate to check if in the circle. The if statement calls for the function and checks the current random point provided.
If this comes back true it adds one to ins variable and one to count. If the function returns false then just add one to count.
When n random points have been checked the program calculates the proportion of points in the circle and multiplies it by 4.
This equation should be approximately pi by the laws of the unit circle. The function returns the approximated pi.
This function is then called to for three different number of point n and stored in the correct variable. I then print
each of the results and the absolute value difference to the correct pi imported from math.


tic_tac_toe.py:

To solve tic_tac_toe i used lists to create 4 rows and updated these lists as the game went on. First i created a function that
prints the board using for loops printing the lists element with a space between. Then i have a function that places a sign on
the desired position of the user. This function uses temporary variables to exchange the correct value in the lists with the players
sign. It check whose turn it is by checking if the round is even or odd and replaces that value in the list and the updates the global
list. I then have two different functions that are the same but one checks if X has won and one checks if O has won. These simply
checks all possible wins for the different players to win and returns true if either has won and false if not. I then have a function
that checks if the desired position is taken or not by checking what value is in the desired position. This function returns true if 
the position is free and false if not. The next function asks the users for input of their desired location. This function also
uses what round it is to check which user to ask for the location. The function returns the desired row and column provided.
I also have a small function that checks whether the desired location even is on the board. The last function checks whether to
end the game by calling the two check if X/O has won or if the board is full hence a draw. This also prints out the result if
it is finished but returns false if it is not time to end. Then comes the basic lists created to build the board with, these
are the lists updated during the game. It then prints the starting board and sets the round to one. I then create a while
loop that keeps going until check_if_end comes back true, by someone winning or a draw. The loop starts off by calling
for the function to ask for player inputs and stores the decided row and column. Then there is two while loops checking if
it's not in board or not taken and if any of them returns false it prints an error message and asks the user for a new input.
If the desired position is not taken and on the board it calls the place function and places the correct sign on the desired location.
Then it calls for the board function that prints the new updated board and then goes on to the next round and the while loop
keeps going until it's time to end.


salary_revision.py:

When solving salary_revision i divided the problem into three different functions that solves each problem provided. 
The first function checks and returns the median of the sorted input. If the function has an even amount of elements the median
is the average of the two elements in the middle. the if statement checks this and computes the median in that case and if its not
even it simply returns the median. The next function calculates the average by taking a for loop and calculating the sum of the list
divided by the amount of elements in list. This then returns the average of the list. The next function checks the gap between the
last and the first element in the sorted list and returns that value. Then comes the main part of the program, it starts by asking 
the user to input the salaries. The input then gets converted into a list which is the sorted by the value from low to high.
We then store each of the values returned from the functions in correct variables. After that it prints out the results.