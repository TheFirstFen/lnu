# Author: Samuel Berg
# Date: 2025-01-29
# For: Task 3 in Assignment 1 in course 2DT906 at LNU
# TODO Completion: WiP!!


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def convert_key(key: str) -> str:
    """
    Converts a string key to a numeric 8-bit key
    Args:
        key (str): The key to convert
    Returns:
        str: The numeric key
    """
    converted_key = ''
    key_len = len(key)

    for char in key:
        converted_key += str(ord(char) + key_len * 217)
        key_len -= 1

    return str(int(converted_key) % 256)


def create_alphabet(key: str) -> str:
    """
    Creates a shifted alphabet based on the input key
    Args:
        key (str): String with numerical value to shift the alphabet by
    Returns:
        str: Shifted alphabet string
    """
    key = int(key) % len(alphabet)
    return alphabet[key:] + alphabet[:key]


def substitution_encrypt(text: str, key: str) -> str:
    """
    Encrypts text using substitution cipher with given key
    Args:
        text (str): String to encrypt
        key (str): Encryption key
    Returns:
        str: Encrypted string
    """
    if key.isalpha():
        key = convert_key(key)

    shifted_alphabet = create_alphabet(key)
    trans_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(trans_table)


def substitution_decrypt(text: str, key: str) -> str:
    """
    Decrypts text that was encrypted using substitution cipher
    Args:
        text (str): String to decrypt
        key (str): Decryption key
    Returns:
        str: Decrypted string
    """
    if key.isalpha():
        key = convert_key(key)

    shifted_alphabet = create_alphabet(int(key))
    trans_table = str.maketrans(shifted_alphabet, alphabet)

    return text.translate(trans_table)


def key_translation(key: str) -> str:   # TODO
    """
    Translates the key to the key that my implementation of transposition cipher can handle
    Args:
        key (str): The key to translate
    Returns:
        str: The new key
    """
    key_length = len(key)
    new_key = ''
    largest = (0,)
    smallest = (10,)
    standard_key = '123'

    if key_length == 1:
        return standard_key[0]

    for i, char in enumerate(key):
        if int(char) > largest[0]:
            largest = (int(char), key_length)
        if int(char) < smallest[0]:
            smallest = (int(char), 1)

    # Handles case of all digits being the same
    if largest[0] == smallest[0]:
        return standard_key[0:key_length]

    """
    Implement something that handles the case where 2 digits are the same within the key.
    Dependent on what the other digit is these same digits should either be replaced '12' or '23' from the standard key
    """

    for i in key:
        if i == str(largest[0]):
            new_key += str(largest[1])
        elif i == str(smallest[0]):
            new_key += str(smallest[1])
        elif key_length == 3:
            new_key += '2'

    return new_key


def transposition_encrypt(text: str, key: str) -> str:
    """
    Encrypts text using columnar transposition cipher while preserving spaces and newlines.
    Args:
        text (str): The plaintext to encrypt
        key (str): The encryption key
    Returns:
        str: The encrypted text with preserved formatting
    """
    if key.isalpha():
        key = convert_key(key)

    if key.count('1') != 1 or key.count('2') != 1 or key.count('3') != 1:
        key = key_translation(key)

    key_order = [int(i)-1 for i in key]
    key_length = len(key_order)

    num_rows = (len(text) + key_length - 1) // key_length

    padding_length = num_rows * key_length - len(text)
    text = text + " " * padding_length

    matrix = []
    for i in range(0, len(text), key_length):
        matrix.append(list(text[i:i+key_length]))

    ciphertext = ""
    for col in range(key_length):
        current_col = key_order.index(col)
        for row in range(num_rows):
            ciphertext += matrix[row][current_col]

    return ciphertext


def transposition_decrypt(text: str, key: str) -> str:
    """
    Decrypts text that was encrypted using columnar transposition cipher.
    Preserves original spacing and newlines.
    Args:
        text (str): The encrypted text
        key (str): The encryption key
    Returns:
        str: The decrypted text with preserved formatting
    """
    if key.isalpha():
        key = convert_key(key)

    if key.count('1') != 1 or key.count('2') != 1 or key.count('3') != 1:
        key = key_translation(key)

    key_order = [int(i)-1 for i in key]
    key_length = len(key_order)

    num_rows = len(text) // key_length

    matrix = [['' for _ in range(key_length)] for _ in range(num_rows)]

    pos = 0
    for col in range(key_length):
        current_col = key_order.index(col)
        for row in range(num_rows):
            matrix[row][current_col] = text[pos]
            pos += 1

    plaintext = ""
    for row in range(num_rows):
        for col in range(key_length):
            plaintext += matrix[row][col]

    plaintext = plaintext.rstrip()

    return plaintext


def main():
    op = input("Do you want to encrypt (E) or decrypt (D)? ").upper()
    method = input(
        "Do you want to use substitution (S) or transposition (T)? ").upper()
    key = input("Input the secret key: ")
    filename = input("Input the name of the file you want to process: ")

    with open('./input/' + filename, 'r') as file:
        text = file.read()

    if method == 'S':
        if op == 'E':
            processed_text = substitution_encrypt(text, key)
        elif op == 'D':
            processed_text = substitution_decrypt(text, key)
        else:
            print("Invalid operation. Please choose either E or D.")
            return
    elif method == 'T':
        if op == 'E':
            processed_text = transposition_encrypt(text, key)
        elif op == 'D':
            processed_text = transposition_decrypt(text, key)
        else:
            print("Invalid operation. Please choose either E or D.")
            return
    else:
        print("Invalid method. Please choose either S or T.")
        return

    output_filename = filename.split(
        '.')[0] + '_enc.txt' if op == 'E' else filename.split('.')[0] + '_dec.txt'
    with open('./output/' + output_filename, 'w') as file:
        file.write(processed_text)

    print(f"The file has been processed and the results have been saved in the file {
          output_filename}")


if __name__ == "__main__":
    main()
