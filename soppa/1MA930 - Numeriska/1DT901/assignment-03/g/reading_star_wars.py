import os
import character as Character


# Creates a list of each line and uses character to create characters in file
def reading(path, name):
    with open(path + "/files2read/" + name, "r") as file:
        for line in file:
            line.strip()
            lst = line.split(", ")
            # Gets function to_row from character
            print(Character.Character(lst[0], lst[1], lst[2]).to_row(), end="")
    print()


print("A collection of Star Wars characters:")
reading(os.getcwd(), "starwars.txt")
