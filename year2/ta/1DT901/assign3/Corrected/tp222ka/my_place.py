import os


# Returns the number of directories
def count_directories(dir_path):
    count_dir = 0
    # loop through entry in the current file
    for entry in os.scandir(dir_path):
        if entry.is_dir():  # if the entry is a directory
            count_dir += 1
            # Recursion continues until there are no more subdirectories
            count_dir += count_directories(entry.path)
    return count_dir


# Returns the number of files
def count_files(dir_path):
    file_count = 0
    for entry in os.scandir(dir_path):
        if entry.is_file():
            file_count += 1
        elif entry.is_dir():
            file_count += count_files(entry.path)
    return file_count


def main():
    # Get current path
    current_dir = os.getcwd()
    # count dir
    dir_count = count_directories(current_dir)
    # count file
    file_counts = count_files(current_dir)
    files = os.listdir(os.curdir)
    # print
    print(files)
    print("I am right now at:", current_dir)
    print(f"Below me I have {dir_count} directories/folders")
    print(f"This directory contains {file_counts} files")


# run the program
main()
