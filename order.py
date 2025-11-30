class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")

        self.customer = customer
        self.coffee = coffee
        self.price = float(price)

        Order.all.append(self)