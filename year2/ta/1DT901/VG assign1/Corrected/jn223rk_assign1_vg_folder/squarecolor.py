if __name__ == "__main__":
    position = input("Enter a chess square identifier (e.g. e5): ")
    letter = position[0]
    number = int(position[1])
    letters = "abcdefgh"
    identity = ""

    # Condition to see that the first character is within a to h and
    # the second character is in the range 1-8
    if letter in letters and number >= 1 and number <= 8:
        # If the letter's index in letters is even
        # and the number is even then the square's color is white
        if letters.find(letter) % 2 == 0 and number % 2 == 0:
            identity += "{} is white".format(position)
        # If the letter's index in letters is odd
        # and the number is odd then the square's color is white
        elif letters.find(letter) % 2 == 1 and number % 2 == 1:
            identity += "{} is white".format(position)
        # If the letter's index in letters is even
        # and the number is odd then the square's color is black
        elif letters.find(letter) % 2 == 0 and number % 2 == 1:
            identity += "{} is black".format(position)
        # If the letter's index in letters is odd
        # and the number is even then the square's color is black
        elif letters.find(letter) % 2 == 1 and number % 2 == 0:
            identity += "{} is black".format(position)

        print("\n", identity, sep="")
