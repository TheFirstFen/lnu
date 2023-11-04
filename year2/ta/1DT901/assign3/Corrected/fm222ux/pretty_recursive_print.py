# Import os module
import os


# Function to print directories beautifully
def pretty_print(dir_path, depth):
    i = depth * "  "
    entries = os.scandir(dir_path)
    for item in entries:
        if item.is_dir():
            print(i + item.name)
            depth += 1
            pretty_print(item, depth)
            depth -= 1


# Get current working directory
dir_path = os.getcwd()

# Start value for depth
depth = 0

# Result
pretty_print(dir_path, depth)
