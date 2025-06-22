class Phone(Item):

    def __init__(self, name, price=0, quantity=0, broken_phones=0):
        # Validation of values provided
        # Super is a special keyword which is required to inherit all the values for the parent class which is needed by the child class.

        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"broken_phone is less than zero"
        # Assigning values
        self.broken_phone = broken_phones