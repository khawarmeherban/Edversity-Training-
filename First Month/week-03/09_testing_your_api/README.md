## Question 01
How do we test an API using pytest?

### Solution
We send HTTP requests to the app using `TestClient` and assert expected status codes and JSON payloads.

### Example
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
response = client.get('/health')
assert response.status_code == 200
```

### Expected Output
All tests pass when the endpoint behaves as expected.
