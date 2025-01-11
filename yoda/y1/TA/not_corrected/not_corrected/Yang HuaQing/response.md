Grade: B
no encryption of password
no validation in regestration 
When you gather the userid it should be "SELECT userid FROM members WHERE email = %s AND password = %s" otherwise when u take response[0] you get the value, which messes with the database it self later on in the program (i will not deduct points from this as this is a very minior mistake)

When displaying the books you should display max 2 books per page not all the books on the choosen subject.
When trying to add a book that does not exist it gives out an error to the user this should not be the case you should validate that the book exists first before trying to add it to the cart. 

Otherwise it looked good well done.