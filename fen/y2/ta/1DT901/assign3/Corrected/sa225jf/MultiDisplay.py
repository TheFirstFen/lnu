class MultiDisplay:
    # Two category variables for message body and frequency impressions.
    message = str()
    count  = int()
    # cod for get back a messeage
    def set_message(self, message: str):
        self.message = message
    #How to determine the number of views
    def set_count(self, count: str):
        self.count = count
    
   # for return a string representation of an object's state.
    def to_string(self):
        return f'Message: {self.message} , Count: {self.count}'
    
    #Here funktion prints the text of message, repeatedly for a specified number of times, each on a new line."
    def display(self):
        for _ in range(self.count):
            print(self.message)
    
    #funktion How to set the message text and the number of impressions at the same time.
    def set_display(self, message: str, count: int):
        self.set_message(message)
        self.set_count(count)
    
    #funktion for get to the message text
    def get_message(self):
        return self.message
    

