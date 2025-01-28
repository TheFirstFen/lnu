# Writen by Martin Fontin mf223ub@student.lnu.se
import math
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # This function creates a new alphabet using the key
def create_new_alphabet(key):
    new_alphabet = ""
    for key_letter in key:
        if(key_letter not in new_alphabet):
            new_alphabet += key_letter
    new_alphabet = new_alphabet.replace(" ", "")
    for letter in alphabet:
        if(letter not in new_alphabet):
            new_alphabet += letter
        print(new_alphabet)
    return new_alphabet

def substitution_encrypt(plain_text, key):
    # Get new alphabet from key
    new_alphabet = create_new_alphabet(key)
    encrypted_text = ""
    # Exchange each letter witch its new letter from the new alphabet
    for letter in plain_text: 
        if letter.isalpha():
            encrypted_text += new_alphabet[alphabet.index(letter)]
        else:
            encrypted_text += letter
    return(encrypted_text)


def substitution_decrypt(encrypted_text, key):
    # Get new alphabet from key
    new_alphabet = create_new_alphabet(key)

    decrypted_text = ""
    # Exchange each encrypted letter witch its new letter from the alphabet
    for letter in encrypted_text:
        if letter.isalpha():
            decrypted_text += alphabet[new_alphabet.index(letter)]
        else:
            decrypted_text += " "
    return(decrypted_text)

def transposition_encrypt(plain_text, key):
    # Removes any duplicate latters from the key
    new_key = ""
    seen_letters = []
    for letter in key.lower():
        if(letter not in seen_letters):
            seen_letters.append(letter)
            new_key += letter
    # Convert the key to lowercase and then sort
    sorted_key = sorted(new_key)
    # Assigns a number to each letter in the sorted form
    letter_numbers = {letter: i + 1 for i, letter in enumerate(sorted_key)}
    # Create a list of lists for each letter in the key
    transposition_lists = [[] for i in range(len(new_key))]
    # Now assign numbers to letters in the unsorted key
    key_numbers = [letter_numbers[letter] for letter in new_key]
    tot_len = len(plain_text) 
    current_index = 0
    # Append the "matrix" with each letter from the plain text inside a new column
    for i in range(0,tot_len):
                transposition_lists[current_index].append(plain_text[i])
                current_index  += 1   
                if current_index == len(new_key):
                    current_index = 0         
                    

    # Now arange the columns in "correct" order 1 2 3 4 5...
    temp_list = [[] for i in range(len(new_key))]
    for index,list_number in enumerate(key_numbers):
        temp_list[list_number-1] = transposition_lists[index]
    
    # Adds the encrypted letters to a string
    encrypted_text = ""
    for i in range(round(tot_len/len(key_numbers))):
        for sublist in temp_list:
            if i < len(sublist):
                encrypted_text += sublist[i]
    print("encrypted text: "+ encrypted_text)
    return(encrypted_text)


def transposition_decrypt(encrypted_message, key):
    # Removes any duplicate latters from the key
    new_key = ""
    seen_letters = []
    for letter in key.lower():
        if(letter not in seen_letters):
            seen_letters.append(letter)
            new_key += letter
    # Convert the key to lowercase and then sort
    sorted_key = sorted(new_key)
    # Assigns a number to each letter in the sorted form
    letter_numbers = {letter: i + 1 for i, letter in enumerate(sorted_key)}
    # Create a list of lists for each letter in the key
    transposition_lists = [[] for i in range(len(new_key))]
    # Now assign numbers to letters in the unsorted key
    key_numbers = [letter_numbers[letter] for letter in new_key]
    tot_len = len(encrypted_message)
    current_index = 0
    # Append the "matrix" with each letter from the encrypted text inside a new column
    for i in range(0,tot_len):
                transposition_lists[current_index].append(encrypted_message[i])
                current_index  += 1   
                if current_index == len(new_key):
                    current_index = 0         
                    
    # Re order based on key numbers
    temp_list = [[] for i in range(len(new_key))]
    for index,list_number in enumerate(key_numbers):
        temp_list[index] = transposition_lists[list_number-1]

    # Adds the decrypted letters to a string
    encrypted_text = ""
    for i in range(math.ceil(tot_len/len(key_numbers))):
        for sublist in temp_list:
            if i < len(sublist):
                encrypted_text += sublist[i]
    print("decrypted text: "+ encrypted_text)
    return(encrypted_text)


def main():
    print("Menu:")
    print("(1) Substitution encryption")
    print("(2) Substitution decryption")
    print("(3) Transposition encryption")
    print("(4) Transposition decryption")
    user_input = input()

    print("Now provide the key used for encryption/decryption")
    key = input()

    print("Enter the path to the file to encrypt/decrypt (Example: C:/Users/marti/Documents/datasäkerhet/test.txt)")
    input_file = input()
    with open(input_file, "r") as file:
        plain_text = file.read()

    print("Enter the filepath to the output file you want (Example C:/Users/marti/Documents/datasäkerhet/test_encrypted.txt)")
    output_file = input()


    match user_input:
        case "1":
            output = substitution_encrypt(plain_text,key)
            with open(output_file, "w") as file:
                file.write(output)
                print("File is now encrypted decrypted as: " + output_file)
        case "2":
            output = substitution_decrypt(plain_text,key)
            with open(output_file, "w") as file:
                file.write(output)
            print("File is now encrypted decrypted as: " + output_file)

        case "3":
            output = transposition_encrypt(plain_text,key)
            with open(output_file, "w") as file:
                file.write(output)
            print("File is now encrypted decrypted as: " + output_file)

        case "4":
            output = transposition_decrypt(plain_text,key)
            with open(output_file, "w") as file:
                file.write(output)
            print("File is now encrypted decrypted as: " + output_file)

        case _:
            exit("Bad input")




if __name__ == "__main__":
    # C:\Users\marti\Documents\datasäkerhet\test.txt
    # key = "thisISaSUPERsecretANDsecureCIPHER"
    # short_key = "test"
    # plain_text = "This is a test string"
    # encrypted_message = "QUPC PC t HICH SIc"
    # trans_encypted_mesage = "hiT is aste t strsngi"
    # substitution_encrypt(plain_text,key)
    # substitution_decrypt(encrypted_message,key)
    # transposition_encrypt(plain_text,short_key)
    # transposition_decrypt(trans_encypted_mesage,short_key)
    main()