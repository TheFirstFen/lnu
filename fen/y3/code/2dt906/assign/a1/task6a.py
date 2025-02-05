# Author: Samuel Berg
# Date: 2025-01-29
# For: Task 6a in Assignment 1 in course 2DT906 at LNU
# Completion: Done!

def my_hash(line: str) -> int:
    """
    Hash function that returns an integer value between 0 and 255
    Args:
        line (str): The string to hash
    Returns:
        int: The hash value
    """
    hash_value = 5381
    for i, char in enumerate(line):
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
        hash_value = (hash_value * 33) + i
    return hash_value % 256


def main():
    test_text = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n',
                 '\n', 'Hello my name is Samuel Berg, how may I assist you today.',
                 'aaaaa', 'aaaab', 'aaaac', 'aaaad']
    for line in test_text:
        print(f'Hash value for "{line.strip()}": {my_hash(line)}')


if __name__ == '__main__':
    main()
