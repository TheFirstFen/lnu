class MultiD:

    count = int()  # Klassvariabel för antal
    messsage = str()  # Klassvariabel för meddelande

    def message_(self, message: str):
        self.message = message  # Sätter instansens meddelande

    def count_(self, count: int):
        self.count = count  # Sätter instansens antal

# Returnerar en strängrepresentation av instansen
    def string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def disp(self):
        for i in range(self.count):  # Skriver ut meddelandet 'count' gånger
            print(self.message)

    def disp_(self, message: str, count: int):
        self.message_(message)  # Sätter meddelandet med given sträng
        self.count_(count)  # Sätter antalet med givet värde

    def get_message(self):
        return self.message  # Returnerar meddelandet för instansen
