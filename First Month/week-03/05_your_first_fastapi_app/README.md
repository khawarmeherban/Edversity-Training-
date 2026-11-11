## Question 01
What is FastAPI and why is it useful for building APIs?

### Solution
FastAPI is a Python web framework that makes it easy to define routes, validate request data, and return JSON responses with automatic documentation.

### Example
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Expected Output
A JSON response: `{"status": "ok"}`
