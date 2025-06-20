import csv


class Item:
    pay_rate = 0.7  # This is a class level attribute can be accessed by both Item.pay_rate and self.pay_rate.
    all = []  # AN Object dictionary which can be used to store instance created.

    def __init__(self, name: str, price: float, quantity=0):
        # Validation of values provided
        assert price >= 0, f"Price is less than zero"
        assert quantity >= 0, f"Quantity is less than zero"

        # Assigning values
        self.name = name
        self.price = price
        self.quantity = quantity

        # Storing all the instances
        Item.all.append(self)  # creating an object to store all the instance created

    def calculated_price(self):
        return self.price * self.quantity

    @classmethod
    def creating_from_csv(cls):
        with open('Objects.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                item["name"],
                float(item["price"]),
                int(item["quantity"])
            )

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    all = []

    def __init__(self, name, price=0, quantity=0, broken_phones=0):
        # Validation of values provided
        # Super is a special keyword which is required to inherit all the values for the parent class which is needed by the child class.

        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"broken_phone is less than zero"
        # Assigning values
        self.broken_phone = broken_phones

        # Storing all the instances
        Phone.all.append(self)  # creating an object to store all the instance created


class Laptop(Item):
    all = []

    def __init__(self, name, price=0, quantity=0, size=13):
        super().__init__(name, price, quantity)
        self.size = size

        Laptop.all.append(self)


phone1 = Phone("Samsung", 25000, -1)
laptop1 = Laptop("Asus", 100000, 5, size=16)

print(Item.all)
print(Phone.all)
print(Laptop.all)

# Documentation
# Assert is user to create custom exceptions to check statements.
# Magic attribute (Item.__dict__) is used to print all the attribute that the class or instance contains
# This magic attribute print both instance level attribute and class level attribute.
# DictReader is a csv function which can be used to read CSV in form of dcitionary which takes the first rows as key and remaining as columns heads can also be added like this => reader = csv.DictReader(file, fieldnames=["name", "age", "city"])
