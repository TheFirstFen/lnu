
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def create_alphabet(key: str) -> str:
    """
    Creates a shifted alphabet based on the input key
    Args:
        key (str): String with numerical value to shift the alphabet by
    Returns:
        Shifted alphabet string
    """
    key = int(key) % len(alphabet)
    return alphabet[key:] + alphabet[:key]


def substitution_encrypt(text: str, key: str) -> str:
    """
    Encrypts text using substitution cipher with given key
    Args:
        text (str): String to encrypt
        key (str): Integer encryption key
    Returns:
        str: Encrypted string
    """
    shifted_alphabet = create_alphabet(int(key))
    trans_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(trans_table)


def substitution_decrypt(text: str, key: str) -> str:
    """
    Decrypts text that was encrypted using substitution cipher
    Args:
        text (str): String to decrypt
        key (str): Integer decryption key (same as encryption key)
    Returns:
        str: Decrypted string
    """
    shifted_alphabet = create_alphabet(int(key))
    trans_table = str.maketrans(shifted_alphabet, alphabet)

    return text.translate(trans_table)


def transposition_encrypt(text: str, key: str) -> str:
    """
    Encrypts text using columnar transposition cipher while preserving spaces and newlines.
    Args:
        text (str): The plaintext to encrypt
        key (str): The encryption key (will be converted to numeric key)
    Returns:
        str: The encrypted text with preserved formatting
    """
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
        key (str): The encryption key (will be converted to numeric key)
    Returns:
        str: The decrypted text with preserved formatting
    """
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

    with open(filename, 'r') as file:
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
    with open(output_filename, 'w') as file:
        file.write(processed_text)

    print(f"The file has been processed and the results have been saved in the file {
          output_filename}")


if __name__ == "__main__":
    main()
