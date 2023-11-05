from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def set_message(self, message):
        self.message = message

    def set_count(self, count):
        self.count = count

    def set_display(self, msg: str, count: int):
        self.set_message(msg)
        self.set_count(count)
        self.display()

    def get_message(self):
        return self.message

    def display(self):
        for _ in range(self.count):
            print(self.message)

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"
