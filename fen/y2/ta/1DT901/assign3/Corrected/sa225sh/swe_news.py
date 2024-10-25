import os


def get_words(input_file):
    with open(input_file, "r", encoding="utf-8", errors="replace") as file:
        seq = file.read().lower()
    extra_characters = "0123456789!@#$%^&*()-_=+[]{};:,.<>?/\\|`~"
    cleaned_seq = ''.join(char for char in seq if char not in extra_characters)
    clean = cleaned_seq.split()
    return clean


def save_words(path, output_path, lst):
    output_file = path + output_path
    with open(output_file, "w", encoding="utf-8", errors="replace") as file:
        for word in lst:
            file.write(word + '\n')
    print("DONE")


def read_file(input_file):
    with open(input_file, "r",  encoding="utf-8", errors="replace") as file:
        file_content = file.read()
        return file_content


path = os.getcwd()
# Delade filen till 8 mindre filer
# därför används forloop för att få datan
for s in range(1, 9):
    input_path = f"\Sa225sh_assign3\input\swe_news{s}.txt"
    output_path = "\Sa225sh_assign3\output\output_news2.txt"
    lst = get_words(path, input_path)
    save_words(path, output_path, lst)
