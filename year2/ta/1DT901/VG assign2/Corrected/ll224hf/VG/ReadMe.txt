In this repository you will find the 4 assignments with "Pass with distinction" marks.
    8. Counting Digits (VG)             [Named "countdigits.py]
    9. Birthday (VG)                    [Named "birthday_candles.py]
    13. ABCD (VG)                       [Named "abcd.py]
    14. Calculating Pi (VG)             [Named "pi_approx.py]
    20. Salary (VG)                     [Named "salery_revision.py]
    21. Drunken Sailor (VG)             [Named "drunken_sailor.py]

8. Counting Digits (VG)  
    In this program the problem we had to solve was read any positive number and then find how many digits in this number
    were either odd, even or a zero. I solved this easily by converting the input into a string then going through
    each charecter by themselves converting them back to an integer and using if statements with modulus to check 
    if even, odd or a zero.

9. Birthday (VG)
    This assignment was a bit tricky. We had to  buy boxes of candles, i.o not 1 by 1. And  on that basis write 
    a probram that predetermined how many boxes we would need to buy before each birthday. Reusing the ones
    we didn't use out of the previous box. My math was off at first, but I managed to make it print out the
    right numbers in the end. 

13. ABCD (VG) 
    This assignment we meant to make a program that heavily hinted at 4 nested loops that itterated all
    possible numbers. This is what took most of the work figuring out, but like I said it was heavily
    hinted at in the assignment document. Using this I made the 4 nested loops and in the deepest loop I
    sent the current state to a function that multiplied the first with 1000, 2nd with 100 and so on.
    I then had an if statements check if the current combination satisfied the condition DCBA = 4 * ABCD.

14. Calculating Pi (VG)
    In this assignment we had to calculate an approximate of pi using a square with a radius of 1 with
    a circle inside of it. First I created the dots coordinates in the square using random.uniform,
    then using pythagoras math skills I find the distance that the dot has from origo. Totaling upp
    "n" amount of dots in the circle I can calculate an approximate of pi. 

20. Salary (VG)
    In this assignment we had to read an arbitrary number of integers from the keyboard and find a way
    to work with it, my issue with this assignment was to think of a way to split up these inputs into 
    multiple different ones, a list in this case. handily we did go through exactly how to do this in 
    lecture 6. Using that I managed to create a list based on the input and with this it was easy to
    just make 3 different functions to calculate the values I needed to get, median, average and gap in
    this case.   

21. Drunken Sailor (VG)
    In this assignment we had to make a program that simulated walking drunken sailors on a board that
    is n long in x and y positive and negative direction. Then based on inputs make the sailors walk
    back and forth, standing still not an option. that was also my problem in this assignment as we
    have not looked into all functions that we can use, in this case i ended up using random.choice
    with a list to force the sailor to walk either forward or backward in either the x or y axis.
