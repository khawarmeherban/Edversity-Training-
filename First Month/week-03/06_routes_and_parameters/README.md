## Question 01
What is a route in FastAPI?

### Solution
A route is an endpoint or URL path that the application handles. Example: `/orders` for listing orders and `/customers/{name}/orders` for a customer-specific route.

### Example
```python
@app.get("/orders")
```

### Expected Output
A JSON list or document returned by the route.
