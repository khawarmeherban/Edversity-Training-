# ==================================================
# QUESTION 01: How can we reject bad input using Pydantic?
# ==================================================

# SOLUTION:
from pydantic import BaseModel, Field, ValidationError

class Order(BaseModel):
    customer_name: str = Field(min_length=2)
    quantity: int = Field(ge=1)
    total: float = Field(ge=0)

for payload in [
    {"customer_name": "A", "quantity": 1, "total": 100},
    {"customer_name": "Noor", "quantity": 0, "total": 100},
    {"customer_name": "Noor", "quantity": 2, "total": -1},
]:
    try:
        print(Order(**payload))
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])

# Expected output:
# String should have at least 2 characters
# Input should be greater than or equal to 1
# Input should be greater than or equal to 0
