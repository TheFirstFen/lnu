from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ''
    n: int = ''

    def set_message(self, new):
        self.message = new
        return self.message

    def set_count(self, c):
        self.n = c
        return self.n

    def to_string(self):
        messag = 'Message: ' + self.message
        count = f'Count: {self.n}'
        return messag, count

    def display(self):
        for i in range(0, self.n):
            print(self.message, '\n')
        return self.message

    def set_display(self, new, nm):
        self.message = new
        self.n = nm
        for i in range(0, self.n):
            print(self.message, '\n')
        return self.message

    def get_message(self):
        return self.message
