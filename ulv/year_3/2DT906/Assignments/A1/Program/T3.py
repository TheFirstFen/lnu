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
    cipher_text = ''
    for i in plaintext:
        if i != ' ':
            if i in alphabet:
                cipher_text += key[alphabet.index(i)]
        else:
            cipher_text += ' '
    return cipher_text

def substitution_decrypt(key, cipher_text):
    key = unique_alphabet(key)
    decrypt_text = ''
    for i in cipher_text:
        if i != ' ':
            if i in key:
                decrypt_text += alphabet[key.index(i)]
        else:
            decrypt_text += ' '
    return decrypt_text
    
def transposition_encrypt(key, plaintext):
    pass

def transposition_decrypt(key, cipher_text):
    pass

def text_reader(file_name):
    text = ''
    with open(file_name, "r") as file:
        for line in file:
            text += line.lower()
    
    return text

def main():
    while True:
        key = input("Enter the key: ")
        print(key)
        text = text_reader("../Data/text.txt")

        cipher_substitution = substitution_encryp(key, text)
        print("Encoded text:", cipher_substitution, "\n")

        decrypt_substitution = substitution_decrypt(key, cipher_substitution)
        print("Decoded text:", decrypt_substitution, "\n")

        #cipher_transposition = transposition_encrypt(key, text)
        #print("Transposition Encoded text: ", cipher_transposition, "\n")

        #decrypt_transposition = transposition_decrypt(key, cipher_transposition)
        #print("Transposition Decoded text: ", decrypt_transposition, "\n")

        

if __name__ == "__main__":
    main()