# Coffee Shop

## Overview
This is a simple Python project modeling a Coffee Shop using Object-Oriented Programming (OOP) principles.  
It consists of three main entities:

- **Customer** – represents a customer who orders coffee.
- **Coffee** – represents different coffee types sold at the shop.
- **Order** – represents a customer ordering a coffee at a certain price.

The project demonstrates class creation, object relationships, and simple aggregation methods.

---

## Features

1. **Customer Class**
   - Initialize a customer with a name (1–15 characters).
   - Methods:
     - `orders()` – list all orders placed by the customer.
     - `coffees()` – list all unique coffees the customer has ordered.
     - `create_order(coffee, price)` – create a new order.
     - `most_aficionado(coffee)` – class method to find the customer who spent the most on a specific coffee.

2. **Coffee Class**
   - Initialize a coffee with a name (minimum 3 characters).
   - Methods:
     - `orders()` – list all orders of this coffee.
     - `customers()` – list unique customers who ordered this coffee.
     - `num_orders()` – total number of orders for this coffee.
     - `average_price()` – average price of this coffee based on orders.

3. **Order Class**
   - Initialize an order with a customer, coffee, and price (1.0–10.0).
   - Methods:
     - `get_customer()` – returns the customer object for the order.
     - `get_coffee()` – returns the coffee object for the order.

---


