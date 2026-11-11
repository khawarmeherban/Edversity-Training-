# ==================================================
# QUESTION 01: How do classes and objects help us model real data?
# ==================================================

# SOLUTION:
class Order:
    def __init__(self, customer: str, total: float) -> None:
        self.customer = customer
        self.total = total

    def receipt(self) -> str:
        return f"Order for {self.customer}: Rs {self.total}"

order = Order("Noor Foods", 2500)
print(order.receipt())

# Expected output:
# Order for Noor Foods: Rs 2500
