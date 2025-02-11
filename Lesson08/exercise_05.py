# Qs
# Create a class called Order which stores item & its price
# Use Dunder function __gt__ to convey that:
# order1 > order2 if price of order1 > price of order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


order1 = Order("chips", 100)
order2 = Order("juice", 200)

print(order1 > order2)
