class Name: 
    # two varables have "string"
    first = str()       
    last = str()

    # first name and last
    def get_first_last(self):
        return f"{self.first} {self.last}"
    # will give just first name
    def get_first(self):
        return self.first

    #lastname
    def get_last(self):
       return self.last
       
    def set_first(self, first):
        self.first = first

    def set_last(self, last):
        self.last_name = last

    def get_short_name(self):
        return f"{self.first[0].upper()}. {self.last}"
 


