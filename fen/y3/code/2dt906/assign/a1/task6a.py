def hash(line: str) -> int:
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
