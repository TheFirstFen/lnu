import os


def count_directories(dir_path):
    folder_count = 0
    dirs = os.scandir(dir_path)

    for path in dirs:
        if path.is_dir():
            folder_count += 1
    return folder_count


def count_files(dir_path):
    file_count = 0
    dirs = os.scandir(dir_path)
    for path in dirs:
        if path.is_file():
            file_count += 1
    return file_count


path = os.getcwd()

print(f"I am right now at: {path}")
print(f"Below me I have {count_directories(path)} directories/folders")
print(f"This directory containes: {count_files(path)} files")
