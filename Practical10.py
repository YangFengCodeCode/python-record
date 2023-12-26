class Item:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def setName(self, name):
        self._name = name

    def setPrice(self, price):
        self._price = price

    def displayItem(self):
        print("item name: ", self._name, ", price: ", self._price)

class Customer:
    def __init__(self, name):
        self._name = name
        self._items = []

    def getName(self):
        return self._name

    def getItems(self):
        return self._items

    def setName(self, name):
        self._name = name

    def setItems(self, item):
        self._items = item

    def addItems(self, item):
        self._items.append(item)

    def calculateTotalPrice(self):
        total = 0
        for item in self._items:
            total += item._price
        return total

# main
name = input("Enter a customer name: ")
# constructor class Customer
customer = Customer(name)

while True:
    option = input('Add one item to the customer("Y" to continue, others to to stop)? ')
    if option != 'Y':
        break
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    # constructor class Item
    item = Item(name, price)
    # add item to class customer
    customer.addItems(item)

# print invoice
for item in customer._items:
    item.displayItem()
# print total price
print("Total price: ", customer.calculateTotalPrice())



