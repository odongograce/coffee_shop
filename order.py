class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee

        if price < 1 or price > 10:
            print("Error: price must be between 1 and 10.")
            self.price = 1
        else:
            self.price = price

        Order.all_orders.append(self)

    def get_customer(self):
        return self.customer

    def get_coffee(self):
        return self.coffee

    def display(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"

