import os


def list_dir(dir_path):

    # Returns a list of strings with the names of the directories.

    return [item for item in os.listdir(dir_path)
            if os.path.isdir(os.path.join(dir_path, item))]


def list_files(dir_path):

    # Returns a list of strings with the names of the files.

    return [item for item in os.listdir(dir_path)
            if os.path.isfile(os.path.join(dir_path, item))]


if __name__ == "__main__":
    current_path = "/Users/sofiasvensson/Documents/Programmering"

    while True:
        print(f"\nCurrent Directory: {current_path}")
        print("Options:")
        print("1. List Directories")
        print("2. List Files")
        print("3. Change Directory")
        print("4. Quit")

        choice = input("==> ")

        if choice == "1":
            dirs = list_dir(current_path)
            print("\nDirectories:")
            for d in dirs:
                print(d)

        elif choice == "2":
            files = list_files(current_path)
            print("\nFiles:")
            for f in files:
                print(f)

        elif choice == "3":
            new_dir = input("Enter directory (or .. to move up): ")

            if new_dir == "..":
                # Move up in the directory hierarchy
                current_path = os.path.dirname(current_path)
            else:
                # Combine the current path with the new directory name
                new_path = os.path.join(current_path, new_dir)

                # Check if the new path exists and is a directory
                if os.path.exists(new_path) and os.path.isdir(new_path):
                    current_path = new_path
                else:
                    print("Invalid directory!")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")
