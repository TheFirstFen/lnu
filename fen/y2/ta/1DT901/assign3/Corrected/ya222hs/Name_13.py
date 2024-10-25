class Name:
    # Klassvariabel för sträng
    first = str()
    last = str()

# returnera båda first och last variabl
    def get_first_last(self):
        return f"{self.first} {self.last}"

# returnera firt
    def get_first(self):
        return self.first

# returnera last
    def get_last(self):
        return self.last

# Sätter förnamnet för instansen
    def set_first(self, first):
        self.first = first

# Sätter efternamnet för instansen
    def set_last(self, last):
        self.last = last

# returnera det förta bokstaven i (first) och hela (last)
    def get_short_name(self):
        return f"{self.first[0].upper()}. {self.last}"
