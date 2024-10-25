from dataclasses import dataclass


@dataclass
class MultiDisplay():
    Message: str = ""  # attributes
    Count: int = 0

    # set message
    def set_message(self, m):
        self.Message = m

    # set count
    def set_count(self, c):
        self.Count = c

    # message and count for print
    def to_string(self):
        st = "Message: " + self.Message + ", Count: " + str(self.Count)
        return st

    # prints the message count times
    def display(self):
        for i in range(0, self.Count):
            print(self.Message, end="\n")  # print count times

    # set the message and cound and print message count times
    def set_display(self, m, c):
        self.Message = m  # set attributes
        self.Count = c
        for i in range(0, self.Count):
            print(self.Message, end="\n")  # print count times

    # return message
    def get_message(self):
        return self.Message
