from order import Order

class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
    

    def orders(self):
        result = []
        for order in Order.all_orders:
            if order.coffee == self:
                result.append(order)
        return result

    def customers(self):
        result = []
        for order in self.orders():
            if order.customer not in result:
                result.append(order.customer)
        return result

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0
        total = 0
        for order in orders:
            total += order.price
        return total / len(orders)
    def display(self):
        return f"Coffee({self.name})"

