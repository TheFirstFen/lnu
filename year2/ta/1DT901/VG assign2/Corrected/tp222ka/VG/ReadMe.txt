# Files submitted:
* abcd.py
* birthday_candles.py
* countdigits.py
* drunken_sailor.py
* pi_approx.py
* salary_revision.py


VG: abcd.py

This program simulates all possible combination of (A B C D)
neither A nor D can be zero to find a solution to ABCD * 4 = DCBA. 

"get_number(a, b, c, d)" function take a four digit and return four digit
to the current size position. 

"simulate" function loop trough all posible combination.
Call the "get_number(a, b, c, d)" to get the current size position.
Check if ABCD * 4 = DCBA, find a solution return. 

VG: birthday_candles.py

This program simulates buying candle boxes for a birthdays over 100 years.
Looping through 1-100 using a for loop. Calculate candle needed for the current year.
Check if there is enough of candles needed for each year.
if not then calculate how many box(es) of candle needed for the current year.
If any left over from previous year update to "candle".
If candle is enought for the current year just subtract it from candle.


VG: countdigits.py

This program counts zero, even and odd digits in an Integer number, 
such as 6789500 Zeros: 2 Odd: 3 Even: 2. 

Starting by checking if the input is positive integer, 
initialized zero to count zeros, odd to count odd digits, and even to count even digits.

The while loop iterates through the digits of the integer.
It continues looping until the entire integer is processed,
inside the loop extracts the last digit of an integer using the modulo operator (n % 10). 
Increments each time the digits is zero, odd or even. 
If "n" is zero, it means all digits have been counted. 


VG: drunken_sailor.py

This progam simulating a random movement of "drunk sailors" within a specified boundary
and then calculates the percentage of sailors who fell into the water. 

- rnd_num(): This function generates a random integer between 1 - 4

- direction(): This function determine the direction (left, right, up, or down)
base on "rad_num()"

- walk_step(step): This function simulates sailor movement by calling "direction()"
for a specified number of steps (step), then update sailor position. 

- check_inside(x, y, sise): This function checks if sailor final position is inside
by the given boundery (size) or not.

- simulate(size, step, sailor): This function simulate number of sailors given by user.
Then keep tracks of how many fall into the water and
calculates the percentage of sailor who fell into the water.


VG: pi_approx.py

This program aproximate pi base on the ratio of points inside the circle / Squre.
It generates random points within the unit square,
calculates distances from the origo, and counts points inside the unit circle.

A list, "lst_num", contains values for testing, such as [100, 10000, 1000000].

The program iterates through the list, calculating approximated pi - the actual pi,
and the error for each value of "lst_num".


Vg: salary_revision.py

This program calculates the median, average, and gap of a list of numbers
(salaries in this case).
It takes a space-separated input of salaries and provides the calculated values.
Ensure the input contains valid numbers separated by spaces for accurate results.
