def partial_decrypt(ciphertext, substitutions):
    # Apply given substitutions to the ciphertext
    plaintext = ""
    for char in ciphertext:
        if char in substitutions:
            plaintext += substitutions[char]
        elif char.isalpha():  # Hide letters not substituted yet
            plaintext += '*'
        else:
            plaintext += char  # Preserve non-alphabetic characters like spaces
    return plaintext

# Ciphertext
ciphertext = "W VWDTB SCBAWS STHWZ RY YQXXUZ FCWUK WSSWFGY"

# Initial substitutions based on frequency analysis
substitutions = {
    'W': 'A',  # Most frequent letter, assumed to be 'A'
    'S': 'T',  # Second most frequent, likely 'T'
    'Y': 'S',  # Third most frequent is O but not likely, Next choice is 'S'
    'R': 'I',  # Most likely 'I' due to the word "IS" in the ciphertext

}

# Decrypt with initial substitutions
decrypted_text = partial_decrypt(ciphertext, substitutions)
print("Step 1 - Partial Decryption:", decrypted_text)
