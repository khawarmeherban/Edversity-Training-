"""Daily task: print items over Rs 1,000 and total all four prices."""

items = [
    {"item": "Laptop stand", "price": 1800},
    {"item": "USB cable", "price": 650},
    {"item": "Keyboard", "price": 3200},
    {"item": "Mouse pad", "price": 450},
]

total_price = 0
for product in items:
    total_price += product["price"]
    if product["price"] > 1000:
        print(f"{product['item']}: Rs {product['price']:,}")

print(f"Total price of all items: Rs {total_price:,}")
assert total_price == 6100
