alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print("Enter the path to the file to decrypt (Example: C:/Users/marti/Documents/datasäkerhet/test.txt)")
# input_file = input()
input_file = "W:/Users/martin/Documents/skola/datasäkerhet/vj222hx.txt"
with open(input_file, "r") as file:
    plain_text = file.read()

decrypted_text = ""
for letter in plain_text:
    match letter:
        case "Q":
            decrypted_text += "S"
        case "A":
            decrypted_text += "e"
        case "J":
            decrypted_text += "c"
        case "p":
            decrypted_text += "r"
        case "r":
            decrypted_text += "t"

        # MEssage
        case "K":
            decrypted_text += "m"
        case "t":
            decrypted_text += "a"
        case "c":
            decrypted_text += "g"

        # Top
        case "R":
            decrypted_text += "t"
        case "M":
            decrypted_text += "o"
        case "N":
            decrypted_text += "p"
        # May
        case "j":
            decrypted_text += "m"
        case "y":
            decrypted_text += "y"
        # Only
        case "L":
            decrypted_text += "n"
        case "i":
            decrypted_text += "l"
        # be
        case "v":
            decrypted_text += "b"
        # read
        case "p":
            decrypted_text += "r"
        case "b":
            decrypted_text += "d"
        # Security
        case "q":
            decrypted_text += "s"
        case "U":
            decrypted_text += "u"
        case "f":
            decrypted_text += "i"
        # Passed
        case "N":
            decrypted_text += "p"

        # From text
        case "d":
            decrypted_text += "h"
        case "B":
            decrypted_text += "f"
        case "F":
            decrypted_text += "i"
        case "u":
            decrypted_text += "V"
        case "V":
            decrypted_text += "v"
        case "h":
            decrypted_text += "k"
        case "g":
            decrypted_text += "j"

        case "e":
            decrypted_text += "B"
        case "E":
            decrypted_text += "C"
        case "s":
            decrypted_text += "E"
        case "C":
            decrypted_text += "G"

        case "P":
            decrypted_text += "R"
        case "I":
            decrypted_text += "L" 

        case "W":
            decrypted_text += "W"
        case "w":
            decrypted_text += "w"  
        case "x":
            decrypted_text += "x" 
        # From googeling D$ampden-$Sydney $College $in $Virginia
        case "D":
            decrypted_text += "H" 
        case "S":
            decrypted_text += "A" 
        case "m":
            decrypted_text += "p" 


        case _:
            decrypted_text += letter 

print(decrypted_text)


