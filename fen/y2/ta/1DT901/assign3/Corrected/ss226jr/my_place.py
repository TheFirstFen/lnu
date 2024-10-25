import os


def count_directories(dir_path):
    # The number of directories in the specified path is returned..

    return sum([1 for item in os.listdir(dir_path)
                if os.path.isdir(os.path.join(dir_path, item))])


def count_files(dir_path):  # Returns the number of files in the given path.

    return sum([1 for item in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, item))])


if __name__ == "__main__":
    directory = "/Users/sofiasvensson/Documents/Programmering/assignment-03"
    # gets the current working directory

    num_directories = count_directories(directory)
    num_files = count_files(directory)

    print(f"I am right now at: {directory}")
    print(f"Below me I have {num_directories} directories/folders")
    print(f"This directory contains {num_files} files")
