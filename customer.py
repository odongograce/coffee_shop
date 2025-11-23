from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        if len(name) < 1 or len(name) > 15:
            print("Error: name must be 1-15 characters.")
        else:
            self.name = name
            Customer.all_customers.append(self)

    def orders(self):
        result = []
        for order in Order.all_orders:
            if order.customer == self:
                result.append(order)
        return result

    def coffees(self):
        result = []
        for order in self.orders():
            if order.coffee not in result:
                result.append(order.coffee)
        return result

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        max_total = 0
        top_customer = None
        for customer in cls.all_customers:
            total = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total += order.price
            if total > max_total:
                max_total = total
                top_customer = customer
        return top_customer
