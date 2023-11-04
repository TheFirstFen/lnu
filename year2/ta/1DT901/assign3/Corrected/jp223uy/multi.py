from dataclasses import dataclass


@dataclass
class Multi:  # Always refer to the "ordinarie" by "self."
    message: str = ""  # Message always string
    count: int = 0  # Count always integer

    def set_message(self, mess):
        self.message = mess

    def set_count(self, countmess):
        self.count = countmess

    def display(self):
        for i in range(self.count):  # How many times mess will be printed
            print(self.message)

    def set_display(self, mess, cnt):
        self.message = mess
        self.count = cnt

    def to_string(self):
        print("Message:", self.message + ", Count:", self.count)

    def get_message(self):
        return self.message  # To get mess, return from main
