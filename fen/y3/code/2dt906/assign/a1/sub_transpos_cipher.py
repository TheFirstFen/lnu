def substitution_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) % 256
            encrypted_char = chr((ord(char) + shift) % 256)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def substitution_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) % 256
            decrypted_char = chr((ord(char) - shift) % 256)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def transposition_encrypt(text, key):
    key_length = len(str(key))
    encrypted_text = [''] * key_length
    for i, char in enumerate(text):
        encrypted_text[i % key_length] += char
    return ''.join(encrypted_text)

def transposition_decrypt(text, key):
    key_length = len(str(key))
    decrypted_text = [''] * ((len(text) // key_length) + 1)
    for i, char in enumerate(text):
        decrypted_text[i % len(decrypted_text)] += char
    return ''.join(decrypted_text)

def main():
    operation = input("Do you want to encrypt (E) or decrypt (D)? ").upper()
    method = input("Do you want to use substitution (S) or transposition (T)? ").upper()
    key = input("Input the secret key: ")
    filename = input("Input the name of the file you want to process: ")

    with open(filename, 'r') as file:
        text = file.read()

    if method == 'S':
        if operation == 'E':
            processed_text = substitution_encrypt(text, key)
        else:
            processed_text = substitution_decrypt(text, key)
    elif method == 'T':
        if operation == 'E':
            processed_text = transposition_encrypt(text, key)
        else:
            processed_text = transposition_decrypt(text, key)

    output_filename = filename.split('.')[0] + '_enc.txt' if operation == 'E' else filename.split('.')[0] + '_dec.txt'
    with open(output_filename, 'w') as file:
        file.write(processed_text)

    print(f"The file has been processed and the results have been saved in the file {output_filename}")

if __name__ == "__main__":
    main()
