# Author: Samuel Berg
# Date: 2025-01-29
# For: Made for file comparison for my own sake
# Completion: Done!

def compare_files(file1_path, file2_path):
    """
    Compare the contents of two text files.
    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file
    Returns:
        bool: True if files are identical, False otherwise
    Raises:
        FileNotFoundError: If either file doesn't exist
        IOError: If there's an error reading the files
    """
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            return content1 == content2

    except FileNotFoundError as e:
        print(f"Error: One or both files not found - {e}")
        raise
    except IOError as e:
        print(f"Error reading files - {e}")
        raise


def main():
    try:
        file1_path = "./data/" + \
            input("Input file1 path and name (ex: taskX/filename.txt): ")
        file2_path = "./data/" + \
            input("Input file2 path and name (ex: taskX/filename.txt): ")

        result = compare_files(file1_path, file2_path)
        print("Are the content of the files identical? ", result)

    except (FileNotFoundError, IOError) as e:
        print(f"Comparison failed: {e}")


if __name__ == "__main__":
    main()
