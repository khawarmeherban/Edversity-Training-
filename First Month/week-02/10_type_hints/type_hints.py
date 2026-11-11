# ==================================================
# QUESTION 01: How do we type a function that returns a dictionary?
# ==================================================

# SOLUTION:
from typing import TypedDict

class OrderSummary(TypedDict):
    customer: str
    total: float


def create_summary(customer: str, total: float) -> OrderSummary:
    return {"customer": customer, "total": total}

print(create_summary("Noor Foods", 1500.5))

# Expected output:
# {'customer': 'Noor Foods', 'total': 1500.5}
