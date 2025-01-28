def decrypt_with_substitution(ciphertext, cipher_line):
    # Define the plain and cipher alphabets
    plain_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = cipher_line.lower()
    
    # Create a mapping table for decryption
    decryption_table = str.maketrans(cipher_alphabet, plain_alphabet)
    
    # Decrypt the ciphertext
    plaintext = ciphertext.lower().translate(decryption_table)
    return plaintext.upper()  # Convert back to uppercase to match ciphertext style

# Ciphertext and provided substitution key
ciphertext = "HKPUFCMHY BHDDXZH"
substitution_key = "xgpyhqzirajsbktcludmvenwfo"

# Decrypt the message
decrypted_message = decrypt_with_substitution(ciphertext, substitution_key)
print("Decrypted Message:", decrypted_message)
