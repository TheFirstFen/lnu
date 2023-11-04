Counting Digits
The program converts the input number to a string and iterates over each digit using a for loop.
It determines the type of each digit by checking conditions for zeros and even/odd digits. 
Counts are kept using variables and updated within the loop. The program displays the counts of zeros, odd digits, 
and even digits


Birtyday_Candles
The birthday_candles() function simulates the process of buying boxes of birthday candles for each year of a person's age,
up to 100 years. It iterates over each age from 1 to 100 and keeps track of the total number of boxes bought and 
the number of remaining candles after each year. If there are enough candles for the next year, it calculates the 
number of boxes needed and updates the totals accordingly. Finally, it prints the number of boxes to buy before each 
birthday and the overall totals of boxes bought and remaining candles.


ABCD
The code defines two functions: get_number(a, b, c, d) and main(). The get_number() function converts 
four input digits into a four-digit integer. The main() function uses nested loops to generate all
possible combinations of digits a, b, c, and d within specified ranges. It calls get_number() to
obtain two four-digit numbers, abcd and dcba. If dcba is four times abcd, the values of a, b, c, and d are printed. 
The program terminates after finding the first valid combination. The code is executed when the script is run directly.


Calculating Pi
This program estimates the value of pi using a Monte Carlo simulation. It generates random points within 
a square and checks if each point falls inside the unit circle. The approximation of pi is calculated based 
on the ratio of points inside the circle to the total number of points. The program repeats this process 
for different values of N and displays the approximation and error for each case.


Salary
This code takes a list of salaries as input, and then calculates and prints the median, average, 
and salary gap based on the provided salaries. The calculate_median function sorts the salaries, determines 
the length of the sorted list, and calculates the median by either averaging the two middle values
(if the list length is even) or taking the middle value (if the list length is odd).The calculate_average function 
calculates the average salary by summing up all the salaries and dividing by the number of salaries.
The calculate_salary_gap function finds the minimum and maximum salaries in the list and calculates 
the salary gap by subtracting the minimum salary from the maximum salary.The code prompts the user to input salaries, 
converts the input into a list of integers, and then calls the relevant functions to calculate the median, average, and gap.
Finally, the results are printed out.


Drunken Sailor
This program simulates the movement of drunken sailors on a grid and calculates the 
percentage of sailors who fall into the water. It defines a function called simulate_drunken_sailors 
that takes in parameters for the size of the grid, the number of steps each sailor takes, and the total number of sailors.
Within the function, the sailors' movements are simulated by randomly choosing directions 
(up, down, left, or right) for each step. The function keeps track of the number of sailors 
who fall into the water by checking if their positions go outside the valid boundary of the grid.
After all sailors have completed their steps or fallen into the water, the function returns the count of fallen sailors.
In the main part of the code, the user is prompted to input the size of the grid, the number of steps, 
and the number of sailors. The simulate_drunken_sailors function is then called with these input values, 
and the result is stored in a variable. Finally, the code calculates the percentage of fallen sailors and prints a 
formatted string displaying the total number of sailors, the number of fallen sailors, and the percentage of fallen sailors.