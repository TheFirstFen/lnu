import os


def my_place():
    current_directory = os.getcwd()
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    file_count = count_file(script_directory)
    directory_count = count_directories(script_directory)

    print(f"Current working directory: {current_directory}")
    print(f"Script path: {script_path}")
    print(f"Number of files: {file_count}")
    print(f"Number of directories: {directory_count}")


def count_file(directory):
    amount = 0
    elements = os.listdir(directory)
    for element in elements:
        element_path = os.path.join(directory, element)
        if os.path.isfile(element_path):
            amount += 1
    return amount


def count_directories(directory):
    amount = 0
    elements = os.listdir(directory)
    for element in elements:
        element_path = os.path.join(directory, element)
        if os.path.isdir(element_path):
            amount += 1
    return amount


my_place()
