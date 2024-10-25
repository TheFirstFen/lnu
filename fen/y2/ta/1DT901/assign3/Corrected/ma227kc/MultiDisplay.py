from dataclasses import dataclass


# required class and functions
@dataclass
class MultiDisplay():
    mess: str = ''
    count: int = 0

    def set_message(self, mess1):
        self.mess = mess1

    def set_count(self, count1):
        self.count = count1

    def to_string(self):
        return f"Message: {self.mess}, Count: {self.count}"

    def display(self):
        for i in range(self.count):
            print(self.mess)

    def set_display(self, mess2, count2):
        self.mess = mess2
        self.count = count2
        for i in range(self.count):
            print(self.mess)

    def get_message(self):
        return self.mess
