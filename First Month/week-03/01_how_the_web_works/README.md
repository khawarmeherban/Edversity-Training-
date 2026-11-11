# ==================================================
# QUESTION 01: How does a browser make a request to a web server?
# ==================================================

# SOLUTION:
# A browser sends an HTTP request to a URL. The server reads the method,
# path, headers, and optional body, then returns an HTTP response.
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)
print(response.json()["url"])

# Example output:
# 200
# https://httpbin.org/get
