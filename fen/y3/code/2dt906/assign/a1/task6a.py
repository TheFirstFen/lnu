def old_hash(line):  # From year 1 1DT901 project
    hash_value = 0
    for char in line:
        hash_value += ord(char)
    return (217 + hash_value) % 256


def hash(line):
    # Starting with a prime number
    hash_value = 5381
    for i, char in enumerate(line):
        # Using XOR and bit rotation and prime multiplication
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
        # Position dependency due to +i
        hash_value = (hash_value * 33) + i
    return hash_value % 256
