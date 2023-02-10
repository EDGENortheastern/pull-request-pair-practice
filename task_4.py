class Insect:
    def __init__(self, type=None, age=None, name=None):
        self.type = type
        self.age = age
        self.name = name
    
    def set_type(self, type):
        self.type = type
    
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name