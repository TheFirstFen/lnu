# Author: Samuel Berg
# TODO Date: 2025-0X-XX
# For: Task 5 in Assignment 1 in course 2DT906 at LNU
# TODO Completion: WiP!

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
    with open('./data/task5/mw224hw/mw224hw_tra.txt', 'r') as file:
        text = file.read()

    processed_text = "Stuck!"

    with open('./data/task5/mw224hw/mw224hw_tra_dec.txt', 'w') as file:
        file.write(processed_text)


def main():
    substitution_decrypt()
    print("Substitution decrypted complete!")

    transposition_decrypt()
    print("Transposition decrypted complete!")


if __name__ == "__main__":
    main()
