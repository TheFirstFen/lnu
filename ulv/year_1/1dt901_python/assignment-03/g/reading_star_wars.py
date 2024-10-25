import os

import Character


# Creat a def called starwars with a empty list.
# opens the file where the text is.
# Splits every line att "," in to a list. returns that list. closes the file.
def starwars(path, input_file):
    lst = []
    with open(path + "/" + input_file, "r") as file:
        for line in file:
            a = line.split(", ")
            lst += a
    file.close()
    return lst


# gets path
path = os.getcwd()
# Name where to find the characters.
input_file = '/mapp_star_wars/starwars.txt'

# variable for the function above.
b = starwars(path, input_file)
# Implementing the character file.
s = Character.character()
# variables used for the naming of the caracters.
j = 1
k = 2
# For loop to put the names, kinds and planets to de right person.
for i in range(0, len(b), 3):
    s.name = b[i]
    s.kind = b[j]
    s.planet = b[k]
    j += 3
    k += 3
    # Printing the names.
    print(s.for_reading())
