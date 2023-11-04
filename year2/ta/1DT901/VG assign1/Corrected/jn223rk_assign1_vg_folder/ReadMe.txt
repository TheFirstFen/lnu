sumofthree.py
Calculate the sum of the three digits by first calculating
how many whole times 100 fits into the three digit number, and then get the first digit. 
Then calculate the remainder of the number when divided by 100 and get a number with the last two
digits of the three digit number. Then calculate how many whole times 10 fits into the 
two digit number and get the second digit. To get the third digit take the remainder of
the two digit number when devided by 10. Now the three digits are known and it is now
possible to take the sum. 


change.py:
The program fetches input from the user: price and payment
If the price is greater than the payment than the program ends, If not
it calculates the difference between payment and price, then round it to the nearest integer.
Thereafter the program calculates how many whole times the change fits into 1000 and then the remainder
when divided by 1000 which then becomes the new change, then repeat the same logic down to 1


tax.py:
Calculative a base tax by taking 30% of monthly income.
If the monthly income is greater than or equal to 38 000,
then add the base tax and the multiplication of 0.05 and the difference
of the monthly income and 38_000. To simplify,
tax_38_000 = base_tax + 0.05 * (monthly_income - 38_000)
If the monthly income surpasses 50_000, then
tax_50_000 = tax_38_000 + 0.05 * (monthly_income - 50_000)


squarecolor.py:
Gets input from the user that consists of two characters such that:
The first character is an alphabetic character between a and h.
The second character is an integer in the range 1 to 8.
From the string "abcdegfh" we can extract an index for each letter that is in the range 0 to 7
If the first character's index in letters is even and the value of the second character is even,
then the square's color is white
If the first character's index in letters is odd and the value of the second character is odd,
then the square's color is white
If the first character's index in letters is even and the value of the second character is odd,
then the square's color is black
If the first character's index in letters is odd and the value of the second character is even
then the square's color is black