menu = {
    "Pizza": 200,
    "Burger": 100,
    "Salad": 70,
    "Pasta": 80
}

#Greet
print("Welcome to Python Dev Hotel..!")
print("Check the menu Below")
for x,y in menu.items():
    print(f"{x} is {y}")

order_total = 0

order_one = str(input("Enter the item you want to be sreved. ?\n"))
assert order_one is not str, "The entered value is not right enter the correct value"
order_total += menu.get(order_one)


