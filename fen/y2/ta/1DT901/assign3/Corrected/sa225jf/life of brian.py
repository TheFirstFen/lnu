import os 
#function read a file 
def read_file(p, f_name):
    path_file = os.path.join(p, f_name)
    with open(path_file, "r", encoding='utf-8')  as file:
        cont_fi = file.read()
    
    return cont_fi

# function will clea all symbols and replace a diffrent symbols such as "'" with space
def get_words(path, input_f):
    content_ = read_file(path, input_f)
    no_add = " '()[]{}/?\\/&%¤""½ ½½§''#:*!789@£$10§-_,.+=>|<';¨^~.\\& "
    words = content_.split()
    just_word = [word.strip(no_add).replace("'", " ")for word in words]
    return just_word

#function for saving words
def save_file(path, output_f, word_s):
    output_f = os.path.join(path, output_f)
    with open(output_f, "w", encoding='utf-8') as file:
        for w in word_s:
            file.write(w + "\n")


path = os.getcwd()
input_f = "life_of_brian.txt"
output_f = "output_life.txt"
word_s = get_words(path, input_f)
save_file(path, output_f, word_s)
print("saved", len(word_s), "words in the file",os.path.join( path + output_f))


