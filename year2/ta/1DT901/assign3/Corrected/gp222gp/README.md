# Notes and Explainations for codes for Assignment 3 G Exercises

# my_place
Prints the current path using os.getcwd. 
Counts the directories/folders in a function using .join to keep the full names and adding to the counter.
Counts the files using the same method.
If .join is not used, it will read individual letters in the path instead of the full names
# move_dir
1 Function to print the Main menu, and 3 for options 1-3
When calling the functions for options 1-3 they do their respective tasks:
1: List current directory
2: Change directory with os.chdir, and if changing directory, it keep the previous directory
so that an exeption for "..." can be used to backtrack
3: Lists files in current directory
The interacting function keeps printing the 4 previous functions when the input is equivalent, and stops 
when the input is "4"
# recursive_print
Checks the current path and prints the directories, and using a recursive function is calls itself and
goes deeper into one of the directories to then print the directories of that directory
# read_write
Reads the file by opening it in reading, appending the words to a list and then returning that list
Writes in the output file by opening it in writing and writing the words from the previous functions list
# read_numbers
Reads the numbers from the file by using .isdigit
Makes an extra exception if the number is negative. Adds the numbers to a list that then is used
to calculate the mean of the numbers
Standard Deviation uses the code from the mean function (Could use recursive, but I dont want to change
it now) and then calculates the standard deviation using the list
# life_of_brian
Removes extra symbols (from a list) and replacing them with nothing and adding the leftover words
to a list
The second function writes all the words in a targetted output file, separating them with commas
# news_reader
Uses the same code as life_of_brian but also removes numbers from the text. Very efficient, which is 
surprising!
# different
One function that outputs a list of random numbers
Sorting and removing duplicates is done by turning the list into a set (removes duplicates),
turning it back into a list, and sorting from low to high using the sorted function
# occurences
Another function that creates a list with random numbers (1-10)
The second function creates the dictionary, and uses the list from the previous function to check
the entire list and adding the numbers (1-10) to their respective key in the dictionary. Lastly it
formats the dictionary content to fit what is shown in the exercises description
# Name and Name_Main
Creates a class with Name that the functions inside then can change the elements of according
to the Name_Main inputs. Formatting is done with f"{}". The class elements need to be = str = '' in order
for the A Palmer part to not require an input in nm.Name
# MultiDisplay and MultiMain
Creates a class for multidisplay with functions that format the inputs correctly
# deque skeleton
