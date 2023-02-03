class Item:
# We are using a constructor instead of getting and setting to make you proud of our versatility
    def __init__(self,type,original_price):
        self.type = type
        self.original_price = original_price

    def raise_price(self, num):
        return self.original_price * (1 + num)

    def set_type(self,type):
        self.type = type
    
    def set_original_price(self,original_price):
        self.original_price = original_price

    def get_type(self):
        return self.type

    def get_original_price(self):
        return self.original_price

pencil = Item('pencil', 2.0)
pencil.set_type('pencil')
pencil.set_original_price(2.3)
print(pencil.raise_price(0.3))