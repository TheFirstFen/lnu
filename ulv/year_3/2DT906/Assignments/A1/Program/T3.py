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

    trans_key = ("012", "021", "102", "120", "201", "210")
    key = trans_key[key % 6]
    key_order = [int(i) for i in key]  # Convert to zero-based indices

    text_length = len(plaintext)
    num_cols = len(key_order)
    num_rows = (text_length + num_cols - 1) // num_cols  # Ceiling division

    padding_len = (num_rows * num_cols) - text_length
    plaintext += ' ' * padding_len  # Add padding to fill the matrix

    # Construct the matrix row by row
    matrix = [plaintext[i * num_cols: (i + 1) * num_cols] for i in range(num_rows)]

    cipher_text = ''
    
    # Read columns based on key order
    for col in key_order:
        for row in range(num_rows):
            cipher_text += matrix[row][col]

    return cipher_text

def transposition_decrypt(key, cipher_text):
    key = int(key) % 256

    if key == 0 or len(cipher_text) == 0:
        return cipher_text

    trans_key = ("012", "021", "102", "120", "201", "210")
    key = trans_key[key % 6]
    key_order = [int(i) for i in key]  # Convert to zero-based indices

    num_cols = len(key_order)
    num_rows = len(cipher_text) // num_cols  # Rows calculated based on cipher length

    # Create an empty matrix
    matrix = [[''] * num_cols for _ in range(num_rows)]

    index = 0  # Position in cipher_text

    # Fill the matrix column-wise according to the key order
    for col in key_order:
        for row in range(num_rows):
            matrix[row][col] = cipher_text[index]
            index += 1

    # Read the matrix row-wise to reconstruct plaintext
    decrypt_text = ''.join([''.join(row) for row in matrix])

    return decrypt_text.strip()  # Remove any trailing padding spaces

def text_reader(file_name):
    text = ''
    with open(file_name, "r") as file:
        for line in file:
            text += line
    
    return text

def file_writer(file_name, cipher_text):
    with open(file_name, "w") as file:
        file.write(cipher_text)

def main():
    while True:
        key = input("Enter the key: ")
        print(key)
        text = text_reader("../Data/plaintext.txt")
        print("Original text:\n", text, "\n")

        cipher_substitution = substitution_encryp(key, text)
        print("Encoded text:\n", cipher_substitution, "\n")
        file_writer("../Data/cipher_substitution.txt", cipher_substitution)

        decrypt_substitution = substitution_decrypt(key, cipher_substitution)
        print("Decoded text:\n", decrypt_substitution, "\n")

        cipher_transposition = transposition_encrypt(key, text)
        print("Transposition Encoded text:\n", cipher_transposition, "\n")
        file_writer("../Data/cipher_transposition.txt", cipher_transposition)

        decrypt_transposition = transposition_decrypt(key, cipher_transposition)
        print("Transposition Decoded text:\n", decrypt_transposition, "\n")

if __name__ == "__main__":
    main()