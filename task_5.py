class Item:
    def __init__(self, type=None, original_price=None, price=None):
        self.type = type
        self.original_price = original_price
        self.price = price

    def set_type(self, type):
        self.type = type
    
    def set_original_price(self, original_price):
        self.original_price = original_price
        self.price = original_price

    def raise_price(self, addition):
        self.price = round(self.original_price + addition, 2)

    def get_type(self):
        return self.type

    def get_original_price(self):
        return self.original_price

    def get_price(self):
        return self.price

    def get_cost_of_10(self):
        return self.price*10