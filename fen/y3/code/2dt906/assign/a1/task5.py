# Author: Samuel Berg (Transposition decryption made by ChatGPT)
# Date: 2025-02-04
# For: Task 5 in Assignment 1 in course 2DT906 at LNU
# Completion: Done!

def substitution_decrypt() -> None:
    """
    Decrypts text that was encrypted using substitution cipher
    Args:
        text (str): String to decrypt
        key (str): Encryption key
    Returns:
        str: Decrypted string
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = "wxyzabcdefghijklmnopqrstuv"

    with open('./data/task5/md223rb/md223rb_sub.txt', 'r') as file:
        text = file.read()

    trans_table = str.maketrans(alphabet, shifted_alphabet)
    processed_text = text.translate(trans_table)

    with open('./data/task5/md223rb/md223rb_sub_dec.txt', 'w') as file:
        file.write(processed_text)


def transposition_decrypt() -> None:
    """
    Decrypts text that was encrypted using transposition cipher
    Args:
        text (str): String to decrypt
    Returns:
        str: Decrypted string
    """
    pass
    with open('./data/task5/ms228qc/ms228qc_tran.txt', 'r') as file:
        text = file.read()

    columns = 3
    rows = len(text) // columns
    extra_chars = len(text) % columns

    grid = [''] * columns
    index = 0
    for col in range(columns):
        size = rows + (1 if col < extra_chars else 0)
        grid[col] = text[index:index + size]
        index += size

    plain_text = ''
    for i in range(rows + 1):
        for col in range(columns):
            if i < len(grid[col]):
                plain_text += grid[col][i]
    processed_text = plain_text

    with open('./data/task5/ms228qc/ms228qc_tran_dec.txt', 'w') as file:
        file.write(processed_text)


def main():
    cipher = input("Task5 - Choose cipher S or T: ")
    if cipher.lower() == 's':
        substitution_decrypt()
    elif cipher.lower() == 't':
        transposition_decrypt()
    else:
        print("Invalid input. Please enter either 'S' or 'T'.")
        return
    print("Transposition decrypted complete!")


if __name__ == "__main__":
    main()
