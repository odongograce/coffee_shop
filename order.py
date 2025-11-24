class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee

    

    def get_customer(self):
        return self.customer

    def get_coffee(self):
        return self.coffee

    def display(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"

