
## Returns the hash value of a string as an integer between 0 and 255
def hash(line):
    hash_value = 7759 
    for i, char in enumerate(line):
        hash_value = ((hash_value << 4) + hash_value) ^ ord(char) 
        hash_value = (hash_value * 31) + i
    return hash_value % 256

def main():
    test_text = "This is a test\n of the hash function"
    for line in test_text.split("\n"):
        print(f" {hash(line)}: {line}")

if __name__ == "__main__":
    main()