from customer import Customer
from coffee import Coffee

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 4.5)
alice.create_order(latte, 3.5)
bob.create_order(latte, 6.0)

print("Latte orders:", latte.num_orders())
print("Latte avg price:", latte.average_price())
print("Most aficionado:", Customer.most_aficionado(latte).name)