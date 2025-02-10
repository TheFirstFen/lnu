alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def unique_alphabet(key):

    key = int(key) % 256  
    unique_alphabet = list(alphabet)
    seed = key
    for i in range(len(unique_alphabet) - 1, 0, -1):
        seed = (seed * 1103515245 + 12345) % 256  
        j = seed % (i + 1)
        unique_alphabet[i], unique_alphabet[j] = unique_alphabet[j], unique_alphabet[i]
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
    
    perm = trans_key[key % len(trans_key)]
    cipher_text = ''
    
    for i in range(0, len(plaintext), 3):
        chunk = plaintext[i:i+3]
        while len(chunk) < 3:
            chunk += ' ' 
        cipher_text += ''.join([chunk[int(p)] for p in perm])
    
    return cipher_text

def transposition_decrypt(key, cipher_text):
    key = int(key) % 256

    if key == 0 or len(cipher_text) == 0:
        return cipher_text

    trans_key = ("012", "021", "102", "120", "201", "210")

    perm = trans_key[key % len(trans_key)]
    reverse_perm = [perm.index(str(i)) for i in range(len(perm))]
    
    decrypt_text = ''
    
    for i in range(0, len(cipher_text), 3):
        chunk = cipher_text[i:i+3]
        chunk = ''.join([chunk[reverse_perm[j]] for j in range(len(perm))])
        decrypt_text += chunk
    
    return decrypt_text.strip()

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
        option = input("Do you want to encrypt or decrypt? (E/D): ").upper()
        method = input("Do you want to use substitution or transposition? (S/T): ").upper()
        key = input("Enter the key(int): ")
        file = input("Enter the file name you want to process in the Data folder: ")

        if method == 'T':
            if option == 'E':
                text = text_reader("../Data/" + file)
                cipher_transposition = transposition_encrypt(key, text)
                print("Transposition Encoded text:\n", cipher_transposition, "\n")

            elif option == 'D':
                cipher_transposition = text_reader("../Data/" + file)
                decrypt_transposition = transposition_decrypt(key, cipher_transposition)
                print("Transposition Decoded text:\n", decrypt_transposition, "\n")

            else:
                print("Invalid option")
                continue

        elif method == 'S':
            if option == 'E':
                text = text_reader("../Data/" + file)
                cipher_substitution = substitution_encryp(key, text)
                print("Encoded text:\n", cipher_substitution, "\n")

            elif option == 'D':
                cipher_substitution = text_reader("../Data/" + file)
                decrypt_substitution = substitution_decrypt(key, cipher_substitution)
                print("Decoded text:\n", decrypt_substitution, "\n")

            else:
                print("Invalid option")
                continue
        else:
            print("Invalid option")
            continue

if __name__ == "__main__":
    main()