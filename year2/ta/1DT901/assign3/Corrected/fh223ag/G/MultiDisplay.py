from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0
    fin_message = str
    prnt_lst = list

    def set_message(self, s):  # Set message too entered string
        self.message = s

    def set_count(self, c):  # Set count too entered int
        self.count = c

    def to_string(self):  # Return a string that tells message and count
        return (f"Message: {self.message}, Count: {self.count}")

    def display(self):  # Display the message count times
        for i in range(self.count):
            print(self.message)

    def set_display(self, s, c):  # Display new message and count
        self.message = s
        self.count = c
        for i in range(self.count):
            print(self.message)

    def get_message(self):  # Return active message
        return self.message
