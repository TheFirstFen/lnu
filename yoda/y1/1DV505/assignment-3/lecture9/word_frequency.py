class WordFrequency:
    def __init__(self, word):
        self.word = word
        self.frequency = 1

    def __str__(self):
        return f'{self.word}: {self.frequency}'

    def __hash__(self):
        bit_shifter = 5
        hash_value = 0
        for char in self.word:
            hash_value = ((hash_value << bit_shifter) - hash_value) + ord(char)
        return hash_value

    def __eq__(self, other):
        if isinstance(other, WordFrequency):
            return self.word == other.word
        return self.word == other
