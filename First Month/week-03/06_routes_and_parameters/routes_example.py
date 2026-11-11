# ==================================================
# QUESTION 01: How do we define a path parameter and a query parameter?
# ==================================================

# SOLUTION:
from fastapi import FastAPI

app = FastAPI()


@app.get("/customers/{name}")
def customer_detail(name: str) -> dict[str, str]:
    return {"customer": name}


@app.get("/orders")
def list_orders(status: str | None = None) -> dict[str, str | None]:
    return {"status": status}


print("Routes ready")
