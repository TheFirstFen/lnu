# ChatGPT generated code

def validate_key(key: int):
    if not (0 <= key <= 255):
        raise ValueError("Key must be an 8-bit integer (0-255).")


def transpose_encrypt(text: str, key: int) -> str:
    validate_key(key)
    columns = key % len(text) if len(text) > key else key
    grid = [''] * columns

    for i, char in enumerate(text):
        grid[i % columns] += char

    return ''.join(grid)


def transpose_decrypt(cipher_text: str, key: int) -> str:
    validate_key(key)
    columns = key
    rows = len(cipher_text) // columns
    extra_chars = len(cipher_text) % columns

    grid = [''] * columns
    index = 0
    for col in range(columns):
        size = rows + (1 if col < extra_chars else 0)
        grid[col] = cipher_text[index:index + size]
        index += size

    plain_text = ''
    for i in range(rows + 1):
        for col in range(columns):
            if i < len(grid[col]):
                plain_text += grid[col][i]

    return plain_text


def main():
    mode = input("Enter mode (e/d): ").strip().lower()
    with open('./data/task5/ms228qc/ms228qc_tran.txt', 'r') as file:
        text = file.read()
    key = int(input("Enter 8-bit key (0-255): ").strip())

    if mode == 'e':
        result = transpose_encrypt(text, key)
    elif mode == 'd':
        result = transpose_decrypt(text, key)
    else:
        print("Invalid mode.")
        return

    with open('./data/task5/ms228qc/ms228qc_tran_dec.txt', 'w') as file:
        file.write(result)


if __name__ == "__main__":
    main()
