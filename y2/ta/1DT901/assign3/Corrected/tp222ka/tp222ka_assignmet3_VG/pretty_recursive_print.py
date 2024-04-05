import os


# Prints the directory structure
def pretty_print(dir_path, depth):
    # List directory entries using os.scandir
    for entry in os.scandir(dir_path):
        # If entty is directory
        if entry.is_dir():
            # Space based on depth
            print(" " * depth, end="")
            print(entry.name)  # Print the name
            # Recursively call the sub-directory with an incremented depth
            pretty_print(entry.path, depth + 1)


# Get the current working directory.
current_path = os.getcwd()
# Call the pretty_print function, starting at depth 0
pretty_p = pretty_print(current_path, 0)
