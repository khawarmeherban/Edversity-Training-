# ==================================================
# QUESTION 01: How do we validate a request model with Pydantic?
# ==================================================

# SOLUTION:
from pydantic import BaseModel, Field, ValidationError


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2)
    item: str = Field(min_length=2)
    total: float = Field(ge=0)


for payload in [
    {"customer_name": "N", "item": "Rice", "total": 100},
    {"customer_name": "Noor", "item": "Rice", "total": -1},
]:
    try:
        print(OrderCreate(**payload))
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])

# Expected output:
# String should have at least 2 characters
# Input should be greater than or equal to 0
