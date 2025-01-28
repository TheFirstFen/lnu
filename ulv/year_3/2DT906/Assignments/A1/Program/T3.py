import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def create_alphabet(key):
    pass

def substitution_encryp():
    pass

def substitution_decrypt():
    pass

def transposition_encrypt():
    pass

def transposition_decrypt():
    pass

def main():
    while True:
        Input = input("Do you want to encrypt(E) or decrypt(D): ")
        if Input == "E":
            Input = input("Do you want to use a substitution cipher(S) or a transposition cipher(T): ")
            if Input == "S":
                input_key = input("Enter the key: ")
                key_alphabet = create_alphabet(input_key)
                print(key_alphabet)
            elif Input == "T":
                input_key = input("Enter the key: ")
                key_alphabet = create_alphabet(input_key)
                transposition_encrypt(key_alphabet)
        elif Input == "D":
            Input = input("Do you want to use a substitution cipher(S) or a transposition cipher(T): ")
            if Input == "S":
                input_key = input("Enter the key: ")
                key_alphabet = create_alphabet(input_key)
                substitution_decrypt(key_alphabet)
            elif Input == "T":
                input_key = input("Enter the key: ")
                key_alphabet = create_alphabet(input_key)
                transposition_decrypt(key_alphabet)
        else:
            print("Invalid Input")
            continue

if __name__ == "__main__":
    main()