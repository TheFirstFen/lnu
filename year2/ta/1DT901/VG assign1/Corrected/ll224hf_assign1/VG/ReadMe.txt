In this repository you will find the 4 assignments with "Pass with distinction" marks.
    7. Sum of Three (VG)            [Named "sumofthree.py]
    8. Change (VG)                  [Named "change.py]
    14. Taxes (VG)                  [Named "tax.py]
    15. Chess Square Color (VG)     [Named "squarecolor.py]

7. Sum of Three (VG)
    In this assignment I simply used Modulus and Floor division and both at the same time
    to fetch the variables from the 3 digit integer that was in the input.
    To prevent letter inputs I simply made the input defined as an integer, so if letters 
    are used in the input it simply gives an error messege.
    An improvment to this program would be to actually use strings, this was not allowed
    hence this how i solved it. BUT it is currently limited to only solve positive 
    integers from 0 to 999.

8. Change (VG)
    In this assignment I used floor division again to calculate each corosponding
    currency notes or coins that could fit into the corrosponding amount left after the
    change has been calculated, this after it had been rounded to the nearest full kr.
    After this has all been calculated i then printed it all out in the listed sequence
    that looks just like the one in example. ALSO this currently prints the "negative" 
    change if the money given is not enough to cover the total price.

14. Taxes (VG) 
    The main problem for me in this assignment was firstly to figure out how to cumulatively
    calculate the tax after each threshold. The fix was quite easy and to just simply state
    the tax for each threshold then remove it if the total income exceeds it.
    I also added a check to see if the income given is positive or not, if negative it just
    gives a message that the amount you made cannot be taxed.

15. Chess square color (VG)
    Hardest assignment here and I found my solution quite satisfying. I started by simply
    structuring the board using 2 text strings. I identified each rows structure, white firstl
    or black first, and later when input was given I first checked the charecter in the input 
    whether it was a viable square on the chessboard i.o "a" to "h". Then the same with the 
    number i.o "1" to "8". After this had been identified as a valid square on the chessboard
    I identified the row using letter, then the color using the number.