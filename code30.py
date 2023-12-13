
class Customer:
    def __init__(self, name,loyalty = 0):
        self.name = name
        self.loyalty = loyalty

    def updatePoints(self, money):
        if money >= 10:
            self.loyalty += money//10

    def displayPoints(self):
        print(self.name)
        print(self.loyalty)





customer1 = Customer('Rick', 5)
print(customer1.name)
print(customer1.loyalty)
customer1.updatePoints(23)
print(customer1.loyalty)
