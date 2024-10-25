

def read_file(file_path):
    lst = []
    f = open(file_path, "r", encoding='utf-8', errors="ignore")  # for win
    lines = f.readlines()
    f.close
    for line in lines:
        lst.append(line)
    return (lst)


st_brian = set()  # New empty set
for i in read_file('brian_13431_words.txt'):
    st_brian.add(i)
st_news = set()  # New empty set
for i in read_file('swe_15217065_news.txt'):
    st_news.add(i)
print(f"unique words brian {len(st_brian)} unique words news {len(st_news)}")
