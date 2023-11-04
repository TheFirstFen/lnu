///////////////////////Assaignments///////////////////////
1.) abcd.py
2.) birthday_candles.py
3.)countdigits.py
4.)drunken_sailor.py
5.)pi_approx.py
6.)salary_revision.py
///////////////////////Description///////////////////////
1.) I used a quadruple nested loop as hinted in the assaignment to solve the problem since going through all numbers from 1000 to 10000 (excluding 10000) four times for four different digits was needed.
    Then i simply multiplied each digit with 10, 100 or 1000 depending on which placement it should have in the numbers
2.) Using a while loop i made the program add more and more boxes until the number of candles became greater than the birthday and then simply calculated the number of boxes which was needed for this whole problem
3.) Started by saving the input from the user as a string since it's easier to check the length of the value because len() cannot be used with an integer.
    Then 'if' statements were used to check the number of odd, even and zero-digits the input had. Also i made sure to check if the input is a number and not a string or a mixture of both
4.) Using 2D-lists to save the need variables was the optimal choice since it's easy, and as instructed in the assaignment description i made the "sailors" take randomly directed steps.
5.) Did as intructed in the exercise description. To find out if the points are inside the circle i decided that using Pythagorean Theorem is an easy salution since the hypotenuse of a triangle inside a unit circle is a maximum of one
    (because of the radius of the circle). Since the ratio between a circle with R radius and a square with the side 2R is Pi/4 is.
    In this exercise we needed pi so I used 'results = (num / N) * 4' num is the number of points inside the circle and N is the total number.
6.) Took the salaries as one string and later splitted them and added them to a list. The rest was simple math.