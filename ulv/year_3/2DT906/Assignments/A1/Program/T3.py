import math

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def unique_alphabet(key):
    key = int(key) % 256  # Ensure key is within 8-bit range
    unique_alphabet = list(alphabet)
    seed = key
    for i in range(len(unique_alphabet) - 1, 0, -1):
        seed = (seed * 1103515245 + 12345) % 256  
        j = seed % (i + 1)
        unique_alphabet[i], unique_alphabet[j] = unique_alphabet[j], unique_alphabet[i]  # Swap characters
    return ''.join(unique_alphabet)

def substitution_encryp(key, plaintext):
    key = unique_alphabet(key)
    print(key, "\n")
    cipher_text = ''
    for i in plaintext:
        if i in alphabet:
            cipher_text += key[alphabet.index(i)]
        else:
            cipher_text += i
    return cipher_text

def substitution_decrypt(key, cipher_text):
    key = unique_alphabet(key)
    decrypt_text = ''
    for i in cipher_text:
        if i in key:
            decrypt_text += alphabet[key.index(i)]
        else:
            decrypt_text += i
    return decrypt_text
    
def transposition_encrypt(key, plaintext):
    key = int(key) % 256

    if key == 0 or len(plaintext) == 0:
        return plaintext
    
    key = str(key)
    
    if len(key) == 1:
        key = "00" + key

    if len(key) == 2:
        key = "0" + key
    
    key_length = len(key)
    text_length = len(plaintext)
    
    matrix = []
    for i in range(0, text_length, key_length):
        matrix.append(list(plaintext[i:i+key_length]))
    
    cipher_text = ''
    for col in range(key_length):
        for row in range(len(matrix)):
            if col < len(matrix[row]):
                cipher_text += matrix[row][col]
    
    return cipher_text


def transposition_decrypt(key, cipher_text):
    key = int(key) % 256

    if key == 0 or len(cipher_text) == 0:
        return cipher_text
    
    key = str(key)
    
    if len(key) == 1:
        key = "00" + key

    if len(key) == 2:
        key = "0" + key

    key_order = [int(i) - 1 for i in key]
    
    key_length = len((key_order))

    text_length = len(cipher_text)
    num_rows = text_length // key_length
    
    matrix = [['' for i in range(key_length)] for _ in range(num_rows)]

    pos = 0
    for column in range(key_length):
        current_column = key_order.index(column)
        for row in range(len(matrix)):
            matrix[row][current_column] = cipher_text[pos]
            pos += 1

    plain_text = ''
    for col in range(key_length):
        for row in range(len(matrix)):
            if col < len(matrix[row]):
                plain_text += matrix[row][col]
    
    return plain_text

def text_reader(file_name):
    text = ''
    with open(file_name, "r") as file:
        for line in file:
            text += line
    
    return text

def main():
    while True:
        key = input("Enter the key: ")
        print(key)
        text = text_reader("../Data/text.txt")
        print("Original text:\n", text, "\n")

        #cipher_substitution = substitution_encryp(key, text)
        #print("Encoded text:\n", cipher_substitution, "\n")
#
        #decrypt_substitution = substitution_decrypt(key, cipher_substitution)
        #print("Decoded text:\n", decrypt_substitution, "\n")

        cipher_transposition = transposition_encrypt(key, text)
        print("Transposition Encoded text:\n", cipher_transposition, "\n")

        decrypt_transposition = transposition_decrypt(key, cipher_transposition)
        print("Transposition Decoded text:\n", decrypt_transposition, "\n")

if __name__ == "__main__":
    main()