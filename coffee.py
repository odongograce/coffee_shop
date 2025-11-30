from order import Order

class Coffee:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")

        self.name = name
        Coffee.all.append(self)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0

        total = sum(order.price for order in orders)
        return total / len(orders)