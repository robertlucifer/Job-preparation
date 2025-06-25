import csv


class Item:
    pay_rate = 0.7  # This is a class level attribute can be accessed by both Item.pay_rate and self.pay_rate.
    all = []  # AN Object dictionary which can be used to store instance created.

    def __init__(self, name: str, price: float, quantity=0):
        # Validation of values provided
        assert price >= 0, f"Price is less than zero"
        assert quantity >= 0, f"Quantity is less than zero"

        # Assigning values
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Storing all the instances
        Item.all.append(self)  # creating an object to store all the instance created

    def calculated_price(self):
        return self.__price * self.quantity

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

    @property
    def name(self):
        print("this is print line")
        return self.__name

    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        print("this is set line")
        self.__name = value

    #creating a private class

    def __connect(self):
        pass

    def __adding_subject(self):
        pass

    def __sending_to_requested_mail(self, name):
        pass

    def sending_mail_to(self, mail):
        self.__connect()
        self.__adding_subject()
        self.__sending_to_requested_mail(mail)
        print(f"sent email to {mail}")
