import HashSet as hset

# Initialize word set
words_brian = hset.HashSet()   # Create new empty HashSet
words_brian.init()             # Initialize with eight empty buckets

# Initialize word set
words_news = hset.HashSet()   # Create new empty HashSet
words_news.init()             # Initialize with eight empty buckets


def read_file(file_path):
    lst = []
    f = open(file_path, "r", encoding='utf-8', errors="ignore")  # for win
    lines = f.readlines()
    f.close
    for line in lines:
        lst.append(line)
    return (lst)


for i in read_file('brian_13431_words.txt'):
    words_brian.add(i)

print("brian data below:")
print("get_size:", words_brian.get_size())
print("zero_bucket_ratio:", words_brian.zero_bucket_ratio())
print("max_bucket_size:", words_brian.max_bucket_size())

for i in read_file('swe_15217065_news.txt'):
    words_news.add(i)

print("news data below:")
print("get_size:", words_news.get_size())
print("zero_bucket_ratio:", words_news.zero_bucket_ratio())
print("max_bucket_size:", words_news.max_bucket_size())
