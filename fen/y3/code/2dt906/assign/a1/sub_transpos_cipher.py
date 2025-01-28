
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_alphabet(key):
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
    new_alphabet = create_alphabet(key)
    enc_text = ""
    for char in text:
        if char.isalpha():
            enc_text += new_alphabet[alphabet.index(char)]
        else:
            enc_text += char

    return enc_text


def substitution_decrypt(text, key):
    new_alphabet = create_alphabet(key)
    dec_text = ""
    for char in text:
        if char.isalpha():
            dec_text += alphabet[new_alphabet.index(char)]
        else:
            dec_text += char

    return dec_text


def transposition_encrypt(text, key):
    key_len = len(str(key))

    enc_text = [''] * key_len
    for i, char in enumerate(text):
        enc_text[i % key_len] += char

    return ''.join(enc_text)


def transposition_decrypt(text, key):
    key_len = len(str(key))

    dec_text = [''] * ((len(text) // key_len) + 1)
    for i, char in enumerate(text):
        dec_text[i % len(dec_text)] += char

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
