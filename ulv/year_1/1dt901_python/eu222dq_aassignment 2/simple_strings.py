def first_last(n):
    return n[0], n[-1]


def char_types(s):
    a = 0
    b = 0
    for c in s.lower():
        if c in ["a", "e", "i", "o", "u"]:
            a += 1
        else:
            b += 1
    return a, b


def char_symbol_number(s):
    char = 0
    sym = 0
    num = 0
    for c in s.lower():
        if 97 <= ord(c) < 123:
            char += 1
        elif 48 <= ord(c) < 58:
            num += 1
        else:
            sym += 1
    return char, num, sym
# Program starts


n = input("Enter a string: ")
print(first_last(n))

s = input("Enter a string: ")
vowels, cons = char_types(s)
print(f"Number of vowels {vowels} and number of consonants {cons}")

q = input("Enter a string: ")
n_ch, n_nr, n_sy = char_symbol_number(q)
print(f"number of characters {n_ch},",
      f"number of symboles {n_sy}, number of number {n_nr}")
