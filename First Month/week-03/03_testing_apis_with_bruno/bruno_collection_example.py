# ==================================================
# QUESTION 01: How do we describe a Bruno request collection?
# ==================================================

# SOLUTION:
# Bruno stores API requests in `.bru` files and uses environments for base URLs.
collection = {
    "name": "Noor Foods Orders API",
    "environment": "local",
    "baseUrl": "http://127.0.0.1:8000",
}
print(collection)

# Expected output:
# {'name': 'Noor Foods Orders API', 'environment': 'local', 'baseUrl': 'http://127.0.0.1:8000'}
