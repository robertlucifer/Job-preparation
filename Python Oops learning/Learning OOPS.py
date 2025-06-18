class Item:
    pay_rate = 0.7 # This is a class level attribute can be accessed by both Item.pay_rate and self.pay_rate.

    def __init__(self, name : str, price : float, quantity =0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculated_price (self):
        return self.price * self.quantity


item1=Item("Phone", 2, 5)
print(Item.pay_rate)
Item.pay_rate = 50
print(Item.pay_rate)

#Assert is user to create custom expections to check statements.
#Magic attribute (Item.__dict__) is used to print all the attribute that the class or instance contains
    #This magic attribute print both instance level attribute and class level attribute.