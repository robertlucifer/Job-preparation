from Items import Item
from Phone import Phone
from Laptop import Laptop


phone1 = Item("Samsung", 25000)

print(phone1.name)
phone1.name = "Apple"
print(phone1.name)

phone1.sending_mail_to("antonyrobert202@gmail.com")

# Documentation
# Assert is user to create custom exceptions to check statements.
# Magic attribute (Item.__dict__) is used to print all the attribute that the class or instance contains
# This magic attribute print both instance level attribute and class level attribute.
# DictReader is a csv function which can be used to read CSV in form of dictionary which takes the first rows as key and remaining as columns heads can also be added like this => reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

#Property Decorator is used make a method read only, example
# @property
# def name(self):
#     return self._name
# makes the variable self.name read-only but still name can be change outside the class using the item._name = value explicitly
# To make a variable completely private it need to initiated like self.__name = name. Which can used and assigned using methods. The self.__name can be used only in class level.

# A method can be covert into private method by adding __ before. Example __sample(self):