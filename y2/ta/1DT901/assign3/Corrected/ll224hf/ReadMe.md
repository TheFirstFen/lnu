In this repository you will find the 4 assignments with "Pass with distinction" marks.
    4. Pretty recursive print (VG)              [Named "countdigits.py]
    9. Lines of python (VG)                     [Named "birthday_candles.py]
    12. Letter count (VG)                       [Named "abcd.py]

    4. Pretty recursive print (VG)
        This was basically the same as recursive print but with an added indent to make
        the printed outputs more clear of which directory they belong to. Didn't really
        find this to be much of an issue as could simply add a counter for each time
        the function had been called to use that to then indent the printed text.

    9. Lines of pyton (VG)
        In this assignment the main problem I had was figuring out how to strip the lines
        down to where I could count them, but I just ended up using the strip() function.
        Then when itterating through the line I counted every time I stripped.

    12. Letter count (VG)
        In letter count we had to go through the life_of_brian.txt and analyze the text
        by counting the amount of times specific letters showed up. Specifically all normal
        english letters i.e a to z. So i started by constructing a dictionary with 
        dictionary comprehensions. "a" to "z" all with an assigned value of 0.
        I then itterated through the list and every time a character was in the dictionary
        the assigned value got increased by 1. I then displayed a histogram where
        200 occurances of the character would equal 1 star.
