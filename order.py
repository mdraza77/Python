class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

    def __lt__(self, order2):
        return self.price < order2.price


o1 = Order("Kurkure", 20)
o2 = Order("Chai", 50)

print(o1 > o2)
