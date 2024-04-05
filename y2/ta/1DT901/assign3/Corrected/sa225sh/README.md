Letter count (VG):

This script reads text from a file specified by the file variable.
It then counts the occurrences of each letter (a to z) in the text, ignoring case.
It prints the total number of letters and displays a simple histogram where each star represents 100 occurrences of a letter.

Pretty Recursive Print (VG):
This script defines a function print_sub that recursively prints the subdirectories and their contents in a directory specified by dir_path. It takes an additional argument depth to control the indentation level.
It starts from the current working directory and goes through each subdirectory, printing their names with the appropriate indentation.

Lines of Python (VG):
This script counts the total number of lines of code in Python files (.py) within a given directory and its subdirectories.
It defines three functions:
count_py_lines(dir_path): This function counts the lines in Python files by excluding empty lines and lines starting with "#" (comments).
find_files(path): This function finds all Python files in a directory (files ending with ".py").
read_file(path): This function reads the content of a file and splits it into lines.
It calculates and prints the total number of lines in Python files within the specified directory.