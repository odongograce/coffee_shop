from order import Order

class Customer:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")

        self.name = name
        Customer.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spending = {}

        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in spending:
                    spending[order.customer] = 0
                spending[order.customer] += order.price

        if len(spending) == 0:
            return None

        return max(spending, key=spending.get)