from dataclasses import dataclass


@dataclass
class Multi:
    message: str = ""
    count: int = 0

    def set_message(self, msg):
        self.message = msg

    def set_count(self, cnt):
        self.count = cnt

    def to_string(self):
        print("Message:", self.message + ", Count:", self.count)

    def set_display(self, msg, cnt):
        self.message = msg
        self.count = cnt

    def display(self):
        for i in range(self.count):
            print(self.message)

    def get_message(self):
        return self.message
