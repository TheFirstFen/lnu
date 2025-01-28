
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def create_alphabet(key):
    """Creates a new alphabet based on the key.

    Args:
        key (int/str): The key used to create the new alphabet.

    Returns:
        str: The new alphabet.
    """
    new_alphabet = ""
    for c in key:
        if c not in new_alphabet:
            new_alphabet += c

    new_alphabet = new_alphabet.replace(" ", "")

    for c in alphabet:
        if c not in new_alphabet:
            new_alphabet += c

    return new_alphabet


def substitution_encrypt(text, key):
    """Encrypts a text using the substitution cipher method.

    Args:
        text (str): The text to be encrypted.
        key (int/str): The key used to encrypt the text.

    Returns:
        str: The encrypted text.
    """
    new_alphabet = create_alphabet(key)
    enc_text = ""
    for char in text:
        if char.isalnum():
            enc_text += new_alphabet[alphabet.index(char)]
        else:
            enc_text += char

    return enc_text


def substitution_decrypt(text, key):
    """Decrypts a text using the substitution cipher method.

    Args:
        text (str): The text to be decrypted.
        key (int/str): The key used to encrypt the text.

    Returns:
        str: The decrypted text.
    """
    new_alphabet = create_alphabet(key)
    dec_text = ""
    for char in text:
        if char.isalnum():
            dec_text += alphabet[new_alphabet.index(char)]
        else:
            dec_text += char

    return dec_text


def transposition_encrypt(text, key):
    """Encrypts a text using a transposition cipher method.

    Args:
        text (str): The text to be encrypted.
        key (int/str): The key used to encrypt the text.

    Returns:
        str: The encrypted text.
    """
    key_len = len(str(key))

    enc_text = [''] * key_len
    for i, char in enumerate(text):
        enc_text[i % key_len] += char

    return ''.join(enc_text)


def transposition_decrypt(text, key):
    """Decrypts a text using a transposition cipher method.

    Args:
        text (str): The text to be decrypted.
        key (int/str): The key used to decrypt the text.

    Returns:
        str: The decrypted text.
    """
    key_len = len(str(key))
    text_len = len(text)

    filled_rows = text_len % key_len
    row_len = text_len // key_len
    rows = []

    start = 0
    for i in range(key_len):
        if i < filled_rows:
            rows.append(text[start:start + row_len + 1])
            start += row_len + 1
        else:
            rows.append(text[start:start + row_len])
            start += row_len

    dec_text = []
    for i in range(row_len + 1):
        for row in rows:
            if i < len(row):
                dec_text.append(row[i])

    return ''.join(dec_text)


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
