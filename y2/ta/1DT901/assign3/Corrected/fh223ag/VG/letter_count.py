import os
import math

path = os.getcwd() + "/new_life_of_brian.txt"  # Path too read
number_stars = 3  # ammount of XX in final print


def count_letters(dir_path):  # Count the letters
    dct = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
           "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
           "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
           "y": 0, "z": 0}  # dictionary containing each letter
    ft = ""  # later split()
    letters = 0  # letter count
    with open(dir_path, "r") as file:  # safe open of file
        for line in file:
            ft += line  # add each line in read file to string
            n = ft.split("\n")  # Split string into list
        for i in n:  # iterate over each word
            for x in i:  # iterate over each letter
                if x == "-":  # remove - since its not a valid letter
                    continue  # move to next iteration if - found
                else:
                    dct[x] += 1  # Add one occurens to dct
        for v in dct.values():  # number of letters = values of dct
            letters += v
        print(f"Reading from the file: {path}")  # Print read path
        print(f"Total number of letters: {letters}\n")  # print n of letters
    return dct  # Return the dct


def histogram(dct):  # Histogram part
    print(f"Histogram (where each star represents {number_stars * 'X'}"
          " occurences of the given letters)")  # Print explanation
    for k, v in dct.items():  # iterate over all items
        n = v/(10**(number_stars - 1))  # ammount of stars
        print(f"{k} | {math.floor(n) * '*'}")  # round n of stars down


# Main program
histogram(count_letters(path))
