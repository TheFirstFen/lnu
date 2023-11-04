import os


# funktion för att läsa filen life of brian
def read_file(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, "r") as file:
        file_content = file.read()
        return file_content


# funktion för rengöra och ransera allting förutom ord
def get_words(path, input_file):
    file_content = read_file(path, input_file)
    overs = "!12#@3£¤4$%5&6/7{}()8[]=0+?´`^¨~*_><|½§.,:\\;äöå"
    cleaned = ""
    for r in file_content:
        if r not in overs:
            cleaned += r
    cleaned = cleaned.replace("'", "")
    cleaned = cleaned.replace("-", "")
    cleaned = cleaned.split()
    return cleaned


# funktion för spara de rengörande ord i en output file med en ord varje rad
def save_file(path, output_file, words):
    output_file = os.path.join(path, output_file)
    with open(output_file, "w") as file:
        for word in words:
            file.write(word + "\n")


# program start
path = os.getcwd()
input_file = "life_of_brian.txt"
output_file = "output_life_of_brian.txt"
words = get_words(path, input_file)
save_file(path, output_file, words)
print()
print('Saved', len(words), 'words in the file', path + output_file)
print()  # räkna längden av hela filen
