from Items import Item

class Laptop(Item):

    def __init__(self, name, price=0, quantity=0, size=13):
        super().__init__(name, price, quantity)
        self.size = size