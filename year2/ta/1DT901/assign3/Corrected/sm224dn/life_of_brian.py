import os

# Funktion att läsa filen innehåll


def read_file(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, "r") as file:
        return file.read()

# funktion för att rensa och dela upp text i ord


def clean(text):
    overs = "!12#@3£¤4$%5&6/7{}()8[]=0+?´`^¨~*><|½§.,:\;äöå"
    cleaned = "". join([char for char in text if char not in overs])
    cleaned = cleaned.replace("'", "").replace("-", "")
    return cleaned.split()

# funktion för att hämta och rensa ord från fil till en annan fil


def get_words(path, input_file):
    file_content = read_file(path, input_file)
    return clean(file_content)

# Funktion att spara ord i en Fil "text fil"


def save_file(path, output_file, words):
    output_file = os.path.join(path, output_file)
    with open(output_file, "w") as file:
        for word in words:
            file.write(word + "\n")

# här är väggen till fillar , rensad ord filar och vart den ska sparas och
# Förlåt det sättet som man ska spara som finns i mymodell fungerade inte


path = os.getcwd()
input_file = "life_of_brian.txt"
output_file = "data/life_of_brian.txt"
words = get_words(path, input_file)
save_file(path, output_file, words)
# här hur mycket ord som sparades
print('Saved', len(words), 'words in the file', path + output_file)
