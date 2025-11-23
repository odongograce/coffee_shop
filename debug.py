from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")


co1 = Coffee("Latte")
co2 = Coffee("Espresso")


o1 = Order(c1, co1, 3)
o2 = Order(c1, co2, 4)
o3 = Order(c2, co1, 5)


print(c1.coffees())
print(co1.customers())
print(co1.num_orders())
print(co1.average_price())
print(Customer.most_aficionado(co1).name)
