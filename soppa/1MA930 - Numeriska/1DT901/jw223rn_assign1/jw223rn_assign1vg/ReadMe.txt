Assignment 1 - vg tasks

sumofthree.py:
When I solved sum of three I first asked the user to input a three digit integer. 
After receiving the integer I started by figuring out the first digit. To figure that out I 
integer divided the provided integer by 100 and stored that value in first_num. To find the second digit I integer divided the number 
by the 10 so that the third digit becomes a decimal. To then remove the first digit that we already know I subtract it by the value
in first_num multiplied by 10 because it's currently in the ten spot. What is left is the second digit which 
gets stored in second_num. To find the third digit I simply took the whole number and subtracted it with the 
first digit times 100 and the second number times 10 which only leaves the third number which gets stored in third_num.
After all three digits have been stored I calculate the sum of them and print the answer to the user.


Change.py:
To solve the problem i first asked the user to input the price of the item and then the amount of money paid.
After that I remove the price from the payment to figure out how much change to be returned. To avoid
decimals I round the change of to the closest integer. To calculate how many of each bill to return i start with
the biggest bill, 1000 kr bill. I integer divide the change by 1000 to figure out the digit in the 1000 spot and that 
is how many 1000 kr bills to be returned, this is then stored in the variable c_1000. To remove the money already returned I store the value of the bills returned
in mon_ret. This variable will be updated after each bill that has been returned to remove all of the change already
returned. To figure out how many 500 kr bills to return I take all change to be returned subtracted by the amount already
returned and integer divide it by 500, this gets stored in the variable c_500. I then update the mon_ret variable by 
taking the amount of bills to be returned, multiply it by 500 and adding the already previous returned money. 
This approach is done on the rest of the bills and coins. After all bills and coins have been calculated
it prints out how many of their respective bills and coins to be returned and the total amount of change. 


tax.py:
To solve tax.py I first asked the user to input the integer, monthly income to be calculated.
I solved it by first make a function that calculates the tax if the income is under 38000 and
stores it in the value u_tax. If the income is above 38000 the tax on that is a constant which is calculated and stored in tax_38. 
I then calculated the tax on the income above 38000 by subtracting it from the full income, then applying the 35% tax. 
If the value is above 50000 the first 50000 is still to have 30% respectively 35% tax but these values are fixed, the variable
tax_50 stores the combined tax. The variable o_tax stores the value of 40% tax on all of the income above 50000.
I then create an if statement that prints the value of u_tax if income is less than 38000. The next statement 
I create is if the income is between 38000 and 50000 it prints the tax on the first 38000 with 30% tax plus the tax of the income above 38000.
The else statement represents when the income is above 50000 then it prints the value of tax_50 which is the fixed tax of the first 38000 
and the next 12000 to reach 50000. it then adds the 40% tax on all income above 50000.


quadratic.py
When solving quadratic.py I start by importing math to make me able to use square root. 
I ask the user to input the three digits to us in the equations, in this case I want them as float because 
I want to be able to use decimals. I begin by calculating what is going to be under the square root
because this decides how many answers there will be. I make an if statement telling the program
to output that there is only one solution, (-b/c) if a, equals zero and b is not equal to 0.
If the number under the square root is less than zero there is no solution cause then the answer becomes imaginary.
In the other case, if the value under the square root is more than zero there will be two answers to the quadratic equation.
This simply adds the three values to the quadratic equations and stores them in s_1 and s_2. It then prints
the two solutions provided. If both a and b equals to zero the only answer is zero, in this case
it prints that 0 is the only solution. The else statement activates only if the value of the square root equals to 0
because in that case there will only be one answer because -b plus zero equals to the same thing as -b subtracted by 0.
It calculate the answer and prints the one solution calculated.