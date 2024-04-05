import os


def print_sub(dir_path, indent=0):
    print('' * indent + os.path.basename(dir_path))

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            print_sub(item_path, indent + 1)


if __name__ == "__main__":
    start_dir = "/Users/alaa/Desktop/""Inledande Prgrammering/"
    print_sub(start_dir)
