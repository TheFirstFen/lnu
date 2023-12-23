import os
# open the file and will read it 
def read_file(path, file_name):
    f_p = os.path.join(path, file_name)
    with open(f_p, "r", encoding='utf-8') as news_file:
        in_the_fi = news_file.read()
        return in_the_fi


def get_words(path, in_f):
    ko_f = read_file(path, in_f)
    with_out = "{}[])()/&123@£$456%¤#"" ''*^^:;.,_6789010-µ><|½§!?+=*\\-+"                  #clean every rows of this symbols
    resultat = [l for l in ko_f if l not in with_out]                                           # loop for every line which become clean
    resultat = "".join(resultat).replace("\n", "").replace("'", "").replace("-", "").split()           #joning space instead of such as ''',\n, 
    for char in with_out:                                      # loop for every character in with_out symbols
        ko_f = ko_f.replace(char, ' ')
    words = ko_f.split()                                         # split text which there is in the file to words
    return words

def save_file(path, out_f, word_ss):
    out_f = os.path.join(path, out_f)
    with open(out_f, "w", encoding='utf-8') as f:              # open the file and write 
        for word in word_ss:                                    # loop for every word 
            f.write(word + "\n")                                 #here cod will write words then use backeslash

path = os.getcwd()                                               # path where I am
in_f = "swe_news.txt"
out_f = "output_news.txt"
word_ss = get_words(path, in_f)
save_file(path, out_f, word_ss)
print("saved", len(word_ss), "words in the file", os.path.join(path, out_f))