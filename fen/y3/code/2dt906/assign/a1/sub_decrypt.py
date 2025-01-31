# Author: Samuel Berg
# Date: 2025-01-31
# For: Task 5 in Assignment 1 in course 2DT906 at LNU
# Completion: Done!

# For ms228qc's files
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Modify for your shifted alphabet
shifted_alphabet = "hijklmnopqrstuvwxyzabcdefgHIJKLMNOPQRSTUVWXYZABCDEFG"


def substitution_decrypt(text: str) -> str:
    """
    Decrypts text that was encrypted using substitution cipher
    Args:
        text (str): String to decrypt
        key (str): Encryption key
    Returns:
        str: Decrypted string
    """
    trans_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(trans_table)


def main():
    with open('./data/task5/ms228qc_sub.txt', 'r') as file:
        text = file.read()

    processed_text = substitution_decrypt(text)

    with open('./data/task5/ms228qc_sub_dec.txt', 'w') as file:
        file.write(processed_text)

    print("Decryption complete!")


if __name__ == "__main__":
    main()
