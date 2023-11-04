countdigits.py:
Count the amount of digits in an integer by converting the given integer from the user
to a string and check whether each digit is even, odd or zero.


birthday_candles.py:
Iterate through all birthdays between 1 and 100 and begin by calculating the amount of candles left
if the amount is lesser than the birthday's number then purchase an amount box of 24 candles until
the amount of candles is greater than or equal to the birthday's number
by the end sum up the total amount of boxes and the unused candles


abcd.py:
Assume abcd is an integer where a,b,c and d are integers between 0-9 such that dcba = 4 * (abcd).
Iterate between all integers between 1000 and 9999 and convert that integer to a string (abcd), then
make a copy of the string (abcd) reverse it such that the copy string now equals dcba then convert both strings to integers
and check if 4 * abcd == dcba is true, then break out the loop and display the result.


pi_approx.py:
To find an approximation of pi take two variables x and y which will be assigned a random float number between 0 and 1
then check whether sqrt(x^2 + y^2) <= sqrt(1), Since the program only need to check for numbers lesser than or equal to 1
the expression can be rewritten by squaring both sides since sqrt(a) <= sqrt(1), then a <= 1, therefore
sqrt(x^2 + y^2) <= sqrt(1) can be rewritten as x^2 + y^2 <= 1.
--
Iterate through the process n times, where n is an input from the user and if x^2 + y^2 <= 1, then
increment a variable (points_in_quadrant) to keep track of how many times x^2 + y^2 <= 1 out of n
then take a ratio: points_in_quadrant / n.
--
multipy it by 4 since the values of x and y are only in the first quadrant, then get the
approximation of pi, then calculate the error value of the approximation by,
error = abs( pi - approx_pi )


salary_revision.py:
Fetches multiple inputs from the user on a single line seperated by spaces and then split the resulting string
to a list, then calculates the average value, the median value and the gap value (the difference between max and min of list
or max_value - min_value)
--
The average value is calculated by taking the sum of the list divided by the length of the list.
--
The median value is calculated by first sorting the list and then take:
1. The middle value of the sorted list if the length is odd or
2. The sum of the 2 values closest to the middle divided by 2 if the length is even.
--
The gap value is taken by sorting the list then take the difference of the last value and the first value
last_value - first_value


drunken_sailor.py:
Fetches three inputs from the user, the size, amount of steps and amount of sailors
--
then iterate trough all sailors, and for each sailors iterate through all steps, where each step has a direction
such that there are two components, vertical and horizontal, the direction is randomly selected such that it can randomly
walk one step in either the positive vertical or negative vertical or positive horizontal or negative horizontal direction
and if the absolute value of the horizontal or the vertical component is greater than the size value the fall count is
incrementented by 1, to get the fall ratio divide the fall count with the amount of sailors
--
The size increase decreases the odds of falling, the step increase increases the odds of falling and
the amount of sailors offers a larger sample size