class Name:
    def __init__(self, first='', last=''):
        self.first = first
        self.last = last

    def to_string(self):
        return f'{self.first} {self.last}'

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def set_first(self, first):
        self.first = first

    def set_last(self, last):
        self.last = last

    def get_short_name(self):
        if self.first and self.last:
            return f'{self.first[0]}. {self.last[:4]}'
        else:
            return ''
