from dataclasses import dataclass

# A data class representing a message
# and count (of how many times to display the message)


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def set_message(self, s):
        self.message = s

    def set_count(self, n):
        self.count = n

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def display(self):
        for _ in range(self.count):
            print(self.message)

    def set_display(self, s, n):
        self.message = s
        self.count = n
        self.display()

    def get_message(self):
        return self.message
