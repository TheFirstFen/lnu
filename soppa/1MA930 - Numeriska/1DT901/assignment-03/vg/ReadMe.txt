pretty_recursive_print.py:

When solving pretty_recursive_print i began by importing the os library. I then created
a simple help function to check if the entry is hidden. This removes the hidden files
and makes the output look better in my opinion. I then create the main function that
prints each directory under the current path. It uses a for loop to check each input
if it's a directory. In the case it is a directory it prints it and then enters.
It then moves one step in by calling for the same function but adding one tab before the
new directory found. It repeats this until all directions have been found and printed out.
The main part of the program finds my current path and calls the main function with count
equal to zero.


Count_lines.py:

To solve count lines i first imported the os library and then i created a help function 
that counts the amount of lines in a file sent to it. this function goes through each 
line to check that it's not empty and returns the amount of non-empty lines.
I then created another function that goes through each subdirectory and check 
for .py files. When a .py file is found the function
calls for the help function to count the lines in that specific file. With the returned
number it adds it to the total number which gets returned when all directories have been
checked. The main part of the program creates the variable num and then checks my 
current directory. It then calls the function and prints out the returned number.


morse.py:

To solve morse.py i began by creating a simple help function that finds the key connected
to the value provided in dictionary. The next function is for creating morse code from a
normal string. It creates a new empty string and then converts the provided string into
lower case. It then checks each character in the string and by using ascii numbers it checks
whether the character is in the alphabet. If it is in the alphabet it checks the dictionary
to see its value and adds it to the string separated by a whitespace. When all letters have
been checked it returns the new string in morse code. The next function starts by creating
a new empty string and an empty list. It then takes the provided string and converts it
to a list. Then a for loop checks each string in list and using the help function to find
the connected key to that value. It then adds that key to the empty string separated by 
a whitespace. The function then returns the newly created morse code string. Then the main
part of the program starts by creating the morse code dictionary. The user is then asked for
an input which translates to morse code via the functions created. After printing the result
it takes a new input in morse code and prints the correspondent text in "normal language".