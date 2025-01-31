# Author: Samuel Berg
# TODO Date: 2025-0X-XX
# For: Task 5 in Assignment 1 in course 2DT906 at LNU
# TODO Completion: WiP!!


def transposition_decrypt(text: str) -> str:
    """
    Decrypts text that was encrypted using transposition cipher
    Args:
        text (str): String to decrypt
    Returns:
        str: Decrypted string
    """
    pass


def main():
    with open('./data/task5/md223rb_tran.txt', 'r') as file:
        text = file.read()

    processed_text = transposition_decrypt(text)

    with open('./data/task5/md223rb_tran_dec.txt', 'w') as file:
        file.write(processed_text)

    print("Decryption complete!")


if __name__ == "__main__":
    main()
