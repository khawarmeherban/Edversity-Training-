# ==================================================
# QUESTION 01: How do we fetch JSON data from a public API?
# ==================================================

# SOLUTION:
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json()["title"])

# Expected output:
# 200
# delectus aut autem
