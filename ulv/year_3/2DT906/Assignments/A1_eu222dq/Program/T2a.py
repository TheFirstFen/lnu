def decrypt_with_substitution(ciphertext, cipher_line):
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = cipher_line.lower()
    
    decryption_table = str.maketrans(cipher_alphabet, plain_alphabet)
    
    plaintext = ciphertext.lower().translate(decryption_table)
    return plaintext.upper()

ciphertext = "HKPUFCMHY BHDDXZH"
substitution_key = "xgpyhqzirajsbktcludmvenwfo"

decrypted_message = decrypt_with_substitution(ciphertext, substitution_key)
print("Decrypted Message:", decrypted_message)
