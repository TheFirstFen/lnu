class Car:
    def __init__(self, make=None, model=None):
        if isinstance(make, str) and isinstance(model, str):
            self.__make = make
            self.__model = model
        else:
            raise TypeError("Make and model has to be string type")

    def set_make(self, make):
        if isinstance(make, str):
            self.__make = make
        else:
            raise TypeError("Make has to be string type")

    def get_make(self):
        return self.__make

    def set_model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            raise TypeError("Model has to be string type")

    def get_model(self):
        return self.__model

    def __str__(self):
        return f"{self.get_make()} {self.get_model()}"
