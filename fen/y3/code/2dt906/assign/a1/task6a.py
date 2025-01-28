def hash(line):
    hash_value = 0
    for char in line:
        hash_value += ord(char)         # Sum ASCII values
    return (217 + hash_value) % 256     # Modulo 256 for 8-bit output


# Usage function
def hash_file(input_filename):
    with open(input_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                print(f"Line: '{line}' : Hash: {hash(line)}")
