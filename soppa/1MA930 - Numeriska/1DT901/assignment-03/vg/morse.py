# Help function to find key connected to value
def find_key(val, dct):
    for k, v in dct.items():
        if val == v:
            return k


# Returns the morse of each character provided
def return_morse(str, dct):
    m_str = ""
    str = str.lower()
    for char in str:
        # Checks using ascii whether char is in alphabet
        if 97 <= ord(char) <= 122:
            char = dct[char]
            m_str += char + " "
    return m_str


# Returns the "normal string" of morse code entered
def return_norm(str):
    n_str = ""
    lst = []
    lst = str.split()
    for str in lst:
        letter = find_key(str, m_dct)
        n_str += letter + " "
    return n_str


# Morse code dictionary
m_dct = {"a": ".-",     "b": "-...",   "c": "-.-.",
         "d": "-..",    "e": ".",      "f": "..-.",
         "g": "--.",    "h": "....",   "i": "..",
         "j": ".---",   "k": "-.-",    "l": ".-..",
         "m": "--",     "n": "-.",     "o": "---",
         "p": ".--.",   "q": "--.-",   "r": ".-.",
         "s": "...",    "t": "-",      "u": "..-",
         "v": "...-",   "w": ".--",    "x": "-..-",
         "y": "-.--",   "z": "--.."}


str = input("Write a message: ")
m_str = return_morse(str, m_dct)
print("Message in morse code:")
print(m_str)
m_str = input("Write in Morse code: ")
print("Message in plain language:")
n_str = return_norm(m_str)
print(n_str)
