import os


# har använd samma kod i uppgift 7 för uppift 8
# har ändra på lite saker för att koden ska räkna hur många ord snabbare
def read_file(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
        return file_content


def get_words(path, input_file):
    file_content = read_file(path, input_file)
    overs = tuple("!12#@3£¤4$%5&6/7{}()8[]=0+?´`^¨~*'_><|½§.,:\\;-")
    # tuple metod är snabbare än lister

    cleaned = [r for r in file_content if r not in overs]
    # list comprehension snabbare än for in loop
    cleaned = "".join(cleaned).replace("\n", "").replace("'", "").\
        replace("-", "").split()
    # laggt och sammalt alla ersättning i samma rad
    # för att förlätta läsningen av koden
    return cleaned


def save_file(path, output_file, words):
    output_file = os.path.join(path, output_file)
    with open(output_file, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")


path = os.getcwd()
input_file = "swe_news.txt"
output_file = "swe_news_output.txt"
words = get_words(path, input_file)
save_file(path, output_file, words)
print()
print('Saved', len(words), 'words in the file', path + output_file)
print()
