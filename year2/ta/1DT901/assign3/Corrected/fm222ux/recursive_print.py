# Import Os module
import os


# Function to list directories
def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for item in entries:
        if item.is_dir():
            print(item.name)
            print_sub(item)


# Get current working directory
dir_path = os.getcwd()

# Result
print_sub(dir_path)
