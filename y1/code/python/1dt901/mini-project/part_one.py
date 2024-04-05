#!/usr/bin/env python3
import io
import lzma
from typing import Dict, List


def get_words(path: str, file_name: str) -> List[str]:
    with lzma.open(path + "/" + file_name) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8") as text_file:
            return text_file.readlines()


def top_ten(lst: List[str]) -> List[str]:
    items: Dict[str, int] = dict()
    for item in lst:
        items[item] = items.get(item, 0) + 1
    sorted_keys: List[str] = sorted(items, key=items.get, reverse=True)
    top_keys = [key for key in sorted_keys if len(key.rstrip()) > 4][:10]

    return [(key, items[key]) for key in top_keys]


for file_name in ["life_of_brian.txt.xz", "swe_news.txt.xz"]:
    words = get_words("./data", file_name)
    unique_words = len(set(words))
    tt = top_ten(words)

    print(f"=== {file_name} ===")
    print(f" The total amount of unique words were {unique_words}")
    print(" The most used words were")
    for index, value in enumerate(tt):
        print(f"  {index + 1}. {value[0].rstrip()}: {value[1]}")
