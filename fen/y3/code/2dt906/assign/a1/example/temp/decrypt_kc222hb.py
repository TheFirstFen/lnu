alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
print("Enter the path to the file to decrypt (Example: C:/Users/marti/Documents/datasäkerhet/test.txt)")
# input_file = input()
input_file = "C:/Users/marti/Documents/datasäkerhet/kc222hb.txt"
with open(input_file, "r") as file:
    plain_text = file.read()

decrypted_text = ""
for letter in plain_text:
    letter = letter.lower()
    match letter:
        case "x":
            decrypted_text += "s"
        case "j":
            decrypted_text += "e"
        case "h":
            decrypted_text += "c"
        case "w":
            decrypted_text += "r"
        case "y":
            decrypted_text += "t"
        case "r":
            decrypted_text += "m"
        case "f":
            decrypted_text += "a"
        case "l":
            decrypted_text += "g"
        case "y":
            decrypted_text += "t"
        case "t":
            decrypted_text += "o"
        case "u":
            decrypted_text += "p"
        case "r":
            decrypted_text += "m"
        case "3":
            decrypted_text += "y"
        case "s":
            decrypted_text += "n"
        case "q":
            decrypted_text += "l"
        case "g":
            decrypted_text += "b"
        case "w":
            decrypted_text += "r"
        case "i":
            decrypted_text += "d"
        case "z":
            decrypted_text += "u"
        case "n":
            decrypted_text += "i"
        case "u":
            decrypted_text += "p"
        
        case "p":
            decrypted_text += "k"
        case "m":
            decrypted_text += "h"
        case "0":
            decrypted_text += "v"
        case "1":
            decrypted_text += "w"
        case "k":
            decrypted_text += "f"

        
        case "2":
            decrypted_text += "x"
        case "4":
            decrypted_text += "z"


        # Assuimg 6 is 1
        case "6":
            decrypted_text += "1"
        case "5":
            decrypted_text += "0"
        case "7":
            decrypted_text += "2"
        case "8":
            decrypted_text += "3"
        case "9":
            decrypted_text += "4"

        case "a":
            decrypted_text += "5"
        case "b":
            decrypted_text += "6"
        case "c":
            decrypted_text += "7"
        case "d":
            decrypted_text += "8"
        case "e":
            decrypted_text += "9"

        case _:
            decrypted_text += letter

print(decrypted_text)


