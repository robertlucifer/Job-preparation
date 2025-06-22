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
        # self.__class__.__name__ provides the name of the class the method currently in
        return f"{self.__class__.__name__} ({self.name}, {self.price}, {self.quantity})"

