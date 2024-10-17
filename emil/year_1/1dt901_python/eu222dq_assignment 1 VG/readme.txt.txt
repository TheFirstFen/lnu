files submitted: 
	sum_of_three.py
	change.py
	tax.py
	quadratic_equation.py

sum_of_three.py: 
	I take an input from the user as a int and gives it to a variable. 
	The first digit is put into a variable using a division with 100 and inting the number to only get a single digit number. 
	The second digit gets in a variable by first deviding the input by 10 and subtracting that number with the first number*10. 
	The last digit gets in a veriable by taking the input and subtracting it with the first number*100 and the second number*10. 
	To sum the three digits togheter i create a new variable and add the digits togheter. 
	Then i print the sum of the digits to show the answer. 

change.py: 
	First i take two inputs, one as the price and one as the peyment. Both are taken as floats. To calculate how much money that
	should be returned the payment is subtracted with the price. The value is then rounded.
	Variables are created to store the value from a integer division. Another valuble is used to store the remanding money using 
	a modulo equation with the value of each bill or coin correspondingly. 
	Last thing is printing the amount of the different bills and coins that are made to be returned.

tax.py: 
	First a input is taken as an int and stored in a valuble. All money up to 38000 and multiplice that with 0.3 for 30% tax.
	If the money exieds 38 000 but does not exied 50 000 i first calculate the amount of money that should be taxed with the higher 
	rate. Then we take the 38 000 and adds the tax from that amount to the higher taxed money between 38 000 and 50 000. That amount
	of money is taxed with 35%. To calculate the amount of tax needed for people earning over 50 000 we take 38 000 times 0.3 and 
	then 12 000 times 0.35 to calculate the amount of tax that should be added on to the highest paid tax money. To calculate the 
	amount of money that should be taxed with 40% we take the earnings and subtract 50 000. All the tax is then added up and printed. 
	everything is in a if statement which makes it so that if you earn under 38 000 you pay only the lower tax. if you are in the 
	middle bracet you pay the middle tax and if you are in the final part you pay the full tax. 

quadratic_equation.py: 
	First we take three inputs from the user to put in the equations. These are stored in valubles. We then use a if, elif and an 
	else statement. In the if statement we take that the first part under the sqrt should be larger than the second part and A is 
	not 0. This creates a answer with two solutions. On the elif statement we have that the first part under the sqrt is smaler than 
	the second part and A is not 0. This gives an irational number or no real solution. In the else statement we take that A equals 0 
	which gives one solution, namely -c/b.