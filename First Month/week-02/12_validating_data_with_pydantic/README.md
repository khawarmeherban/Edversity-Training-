# ==================================================
# QUESTION 01: What is Pydantic used for?
# ==================================================

# SOLUTION:
# Pydantic validates data and converts it into Python types.
from pydantic import BaseModel, Field, ValidationError

class Order(BaseModel):
    customer_name: str = Field(min_length=2)
    quantity: int = Field(ge=1)
    total: float = Field(ge=0)

try:
    order = Order(customer_name="Noor", quantity=2, total=2500)
    print(order)
except ValidationError as exc:
    print(exc)

# Expected output:
# customer_name='Noor' quantity=2 total=2500.0
