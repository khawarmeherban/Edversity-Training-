# ==================================================
# QUESTION 01: How do we create a Product class with a discount method?
# ==================================================

# SOLUTION:
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def discounted_price(self, percent: float) -> float:
        return self.price * (1 - percent / 100)

p = Product("Rice", 200)
print(p.discounted_price(10))

# Expected output:
# 180.0
