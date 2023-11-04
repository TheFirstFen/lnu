import os


# Räknar mappar
def count_directories(path):
    directories = 0
    lst = os.scandir(path)
    for c in lst:
        if (c.is_dir()):
            directories += 1
    return directories


# Räknar filer
def count_files(path):
    files = 0
    file_lst = os.scandir(path)
    for c in file_lst:
        if (c.is_file()):
            files += 1
    return files


# Main program
# Kör funktionerna
path = os.getcwd()
directories = count_directories(path)
print(f"Directories: {directories}")

files = count_files(path)
print(f"Files: {files}")
