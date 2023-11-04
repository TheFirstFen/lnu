VG
* Sumofthree.py
The program takes a three-digit number, calculates the sum of its individual digits, and prints the result.

The user is prompted to enter a three-digit number using the input() function, 
and the input is converted to an integer and stored in the number variable.
The program calculates the three individual digits of the number using i
nteger division // and the modulus operator %:
- Hundratal = number // 100 calculates the hundreds place digit by dividing the number by 100 and 
rounding down to the nearest integer.
- Tiotal = (number % 100) // 10 calculates the tens place digit. 
It first uses the modulus operator % to get the remainder when dividing the number by 100 
(which removes the hundreds place digit), and then performs integer division by 10 to isolate the tens place digit.
- Ental = number % 10 calculates the units place digit by using the modulus operator % to get 
the remainder when dividing the number by 10.
The program calculates the sum of the three digits by adding hundratal, tiotal, and ental, and 
assigns the result to the variable summa. Finally, the program prints the result using the print() function. 
It displays the message "Sum of digits" followed by the value of summa.



* Change.py
The program takes the price and payment from the user and provides output of the number of Swedish bills and 
coins to be given back as change.

The program prompts the user to enter the price of an item and the payment amount. 
Both values are stored as floating-point numbers in the variables price and payment.
The change is calculated by subtracting the price from the payment, and the result is rounded to the nearest integer. 
The change is stored in the variable change.
A list of denominations for Swedish bills and coins is defined in the variable denominations.
An empty list, change_count, is created to store the count of each denomination in the change.
For each denomination denom in the denominations list:
The count of the current denomination in the change is calculated by performing integer division of change by denom. 
The result is stored in the variable count.
The count of denomination denom is appended to the change_count list using the append() method.
The value of change is updated by subtracting count * denom from change. 
This ensures that the remaining change is correctly used to calculate the next denomination.
Finally, the program prints the change amount and the count of each denomination. 
The change amount is rounded to the nearest integer and displayed along with the denominations in the denominations 
list and the corresponding counts in the change_count list.



* tax.py
This program takes the monthly income as input, calculates the income tax based on the given 
income using if-elif-else statements, and then prints the corresponding income tax.

The program prompts the user to enter the monthly income using the input() function, 
and the input is converted to an integer using int() and stored in the income variable.
The program calculates the income tax based on the provided monthly income using if-elif-else statements:
-If the income is less than 38,000, the tax is calculated by multiplying the income by 0.3 (30%).
-If the income is between 38,000 and 50,000 (inclusive), the tax is calculated by adding two parts: 
30% tax on the income up to 38,000 and 35% tax on the remaining income.
-If the income is above 50,000, the tax is calculated by adding three parts: 
30% tax on the income up to 38,000, 35% tax on the income between 38,000 and 50,000, and 40% tax on the remaining income.
The calculated income tax is stored in the tax variable.
The program prints the corresponding income tax using the print() function, 
displaying the message "Corresponding income tax:" followed by the value of the tax variable.



* squarecolor.py 
The program takes a chess square identifier as input, extracts the file and rank from the identifier, 
determines the color of the square based on the file and rank, and then prints the square identifier along with the color of the square.

The program prompts the user to enter a chess square identifier using the input() function, 
and the input is stored in the square variable.
The program extracts the file (letter) and rank (integer) from the square identifier. 
The file is obtained by accessing the first character of the square string with square[0], 
and the rank is obtained by converting the second character of the square string to an integer using int(square[1]).
The program determines the color of the square based on the file and rank using if-else conditions:
If the file is one of "aceg" (odd columns) and the rank is odd (rank % 2 == 1), 
or if the file is one of "bdfh" (even columns) and the rank is even (rank % 2 == 0), 
the square is considered black. Otherwise, the square is considered white.
The determined color is stored in the color variable.
The program prints the color of the square using the print() function, 
displaying the square identifier followed by the color.

