def get_user_input():
    filename = input("Enter a file name to create (e.g., myfile.txt): ")
    content = []
    print("Enter lines of content. Type 'stop' on a new line to finish.")

    while True:
        line = input()
        if line == "stop":
            break
        content.append(line)

    return filename, "\n".join(content)


def write_file(path, name, content):
    with open(os.path.join(path, name), "w") as file:
        file.write(content)


if __name__ == "__main__":
    import os

    directory_path = os.getcwd()
    filename, content = get_user_input()

    if filename:
        write_file(directory_path, filename, content)
        print(f"File '{filename}' has been created in '{directory_path}'.")
