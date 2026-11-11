# Noor Foods Orders API

## Question 01
How do we design a simple orders API that supports filtering, validation, and a summary endpoint?

### Solution
We create a FastAPI app backed by SQLModel and SQLite by default. Each order stores a customer name, item, quantity, total, status, and creation time. The API provides the list of orders, customer-filtered orders, a summary endpoint, and update/delete operations.

### Example
A request like `GET /orders?customer=noor foods&min_total=500` returns only matching orders.

### Expected Output
A JSON array of order objects.

---

## Question 02
What is the purpose of the `/summary` route?

### Solution
It provides a concise dashboard view for staff: total order count, total revenue, average order value, and number of unique customers. This is useful for monitoring sales and operations.

### Example
`GET /summary` returns data such as:

```json
{
  "total_orders": 12,
  "total_revenue": 15250.0,
  "average_order_value": 1270.83,
  "customers_served": 8
}
```

### Expected Output
A summary payload with numeric totals.

---

## Setup

```powershell
cd "First Month/week-03/12_noor_foods_orders_api"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`
- `GET /orders`
- `GET /customers/{name}/orders`
- `GET /summary`
- `POST /orders`
- `PUT /orders/{id}`
- `DELETE /orders/{id}`

## Validation rules

- customer names must be at least two characters
- order totals can not be negative
- item names cannot be blank
- status must be one of `pending`, `processing`, `delivered`, or `cancelled`

## Deployment notes

The app is PostgreSQL-ready. Set `DATABASE_URL` to a PostgreSQL connection string in production. Local development uses SQLite by default which is useful for tests and quick demos.
