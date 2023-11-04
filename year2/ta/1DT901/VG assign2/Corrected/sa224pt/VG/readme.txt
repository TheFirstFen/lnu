files submited:
abcd.py:
to find the reversed digit that equals 4 times the digit, I started by creating Variables a, b, c and d, Which I assigned their values to be 1000, 100, 10 and 1 respectively. I then created a While loop to iterate through the digits incrementing them and checking if the reversed satisfies the condition.

birthday_candles.py:
started by creating Variables to store the number of leftover candles and number of boxes used, and a Variables to quickly use the number of candles in each bought box, then used a for loop to iterate through the age from 1 to 100 checking if the number of leftover candles is enough for the age, if not I would buy more boxes that are enough for the rest of the age after deducting the leftover candles.

countdigits.py:
after getting the iput number of a user I created 3 Variables to store zeros, odd and even. then used a for loop to iterate through the the number and checked each digit to add it to the correct Variable.

drunken_sailor:
stared by importing random for a random move and storing the size, steps and number of sailors from a user input. I then created a Variable platform to store the movement of each sailor in, and lastly a variable to store the number of drowned sailors. after that I then used a for loop to iterate through the number of sailors giving each of them a new platform to move randomly on, and tracked their movement to see if they fall or not using another for loop for steps.

pi_approx.py:
started by importing random and math to use pi and get random points on the circle. in a new function I created a variable to store the number of points that are inside the circle, using a for loop I iterated through the N number and created x,y with a random.uniform to get a more random number which increases the chances of getting a closer number to pi, I then checked if the equation for the area of the circle is satisfied wich meant the points are inside the circle so I added them to the variable that I created at the beginning, after finishing the for loop I returned the pi approximation by dividing the results by n and multiplying it by 4 (the square area).

salary_revision.py:
first stored the input of user in a variable, then created multiple variable, s_lst: the list of input numbers, median, average, gap and sum which are self explanatory. then using a for loop I converted the input into a list of integers and added it to the created s_lst, while getting the sum of all numbers in the same for loop. then sorted it using the sort function and then started with median, I had to check first if the length of the list is odd or even to know if the median is going to be the middle number of 2 middle numbers divided by2, I then got the median using basic math. For the average I simply got the rounded result of dividing the sum over the length of the list, lastly I got the gap by deducting the last item in the list from the first item (biggest - smallest)
