

Database (20 out of 20 points)

Task 1 Registration,Login, Logout, and Quit  (14 points out of 20):

Task2 Browse and Search (16 points, max 20):

Task3 Cart (15 points, max 20):

*Task4 Checkout  (10 points, max 20):*

Hello Huaqing Yang,

Grade: B

We have now checked your Assignment 2 submission. Below are comments for each task:

*Database (20 out of 20 points)
- The database is correctly configured with primary and foreign keys. 

*Task 1 Registration,Login, Logout, and Quit  (14 points out of 20):*

- no encryption of password
- no validation in regestration 

- When you gather the userid it should be "SELECT userid FROM members WHERE email = %s AND password = %s" otherwise when u take response[0] you get the value, which messes with the database it self later on in the program (i will not deduct points from this as this is a very minior mistake)

Task2 Browse and Search (18 points, max 20):

- When displaying the books you should display max 2 books per page not all the books on the choosen subject.
- When trying to add a book that does not exist it gives out an error to the user this should not be the case you should validate that the book exists first before trying to add it to the cart. 

Task3 Cart (15 points, max 20):

Correctly implemented

Task4 Checkout  (10 points, max 20):

Correctly implemented

Otherwise it looked good well done.