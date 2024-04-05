import os


def print_sub(dir_path, indent=0):
    # print the current directory's name
    print('' * indent + os.path.basename(dir_path))

    # in relation to each item in the current directory
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        # print its content
        if os.path.isdir(item_path):
            print_sub(item_path, indent + 1)


if __name__ == "__main__":
    start_dir = "/Users/sofiasvensson/Documents/Programmering"
    print_sub(start_dir)
