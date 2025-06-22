from Items import Item
from Phone import Phone
from Laptop import Laptop


phone1 = Phone("Samsung", 25000, 1)
laptop1 = Laptop("Asus", 100000, 5, size=16)

print(Item.all)


# Documentation
# Assert is user to create custom exceptions to check statements.
# Magic attribute (Item.__dict__) is used to print all the attribute that the class or instance contains
# This magic attribute print both instance level attribute and class level attribute.
# DictReader is a csv function which can be used to read CSV in form of dcitionary which takes the first rows as key and remaining as columns heads can also be added like this => reader = csv.DictReader(file, fieldnames=["name", "age", "city"])
