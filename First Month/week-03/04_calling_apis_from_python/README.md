## Question 01
How do we call an API from Python?

### Solution
We use the `requests` library to send HTTP requests and parse the JSON response. This is useful for quick integrations and testing.

### Example
```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json()["title"])
```

### Expected Output
`200` and the title of the todo item.
