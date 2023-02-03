class Insect:
    def set_type(self,type):
        self.type = type
    
    def set_age(self,age):
        self.age = age

    def set_name(self,name):
        self.name = name

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

grasshopper_lala = Insect()
grasshopper_lala.set_name('lala')
grasshopper_lala.set_type('grasshopper')
grasshopper_lala.set_age(4)

print(grasshopper_lala.get_type(),grasshopper_lala.get_name(),grasshopper_lala.get_age())
