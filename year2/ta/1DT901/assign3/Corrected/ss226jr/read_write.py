import os


def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    else:
        print(f"Error: File '{file_path}' not found.")
    return None


def write_file(lines, file_path):
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"File successfully written to '{file_path}'.")


if __name__ == "__main__":
    path = '/Users/sofiasvensson/Documents/Programmering/assignment-03'
    input_file_path = os.path.join(path, 'mamma_mia.txt')
    output_file_path = os.path.join(path, 'output_mamma_mia.txt')

    lines = read_file(input_file_path)

    if lines is not None:
        write_file(lines, output_file_path)
