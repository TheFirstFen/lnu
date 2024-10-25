import os


# Funktion som tar fram alla filer och sedan räknar varje rad i alla som inte
# bara är mellanrum

def count_py_lines(dir_path):
    lines = 0
    number_of_files = 0
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if (file.endswith(".py")):
                file_list.append(file)
                number_of_files += 1
    for doc in file_list:
        doc_open = open(doc, "r", encoding="utf-8")
        doc_lines = doc_open.readlines()
        for line in doc_lines:
            for c in line:
                if (c.isalpha()):
                    lines += 1
                    break
        doc_open.close()
    return lines, number_of_files


# Main program

path = os.getcwd()
print("path: ", path)
lines, files = count_py_lines(path)
print(lines, files)
