# ==================================================
# QUESTION 01: How do we represent common HTTP methods in code?
# ==================================================

# SOLUTION:
# REST APIs typically use GET, POST, PUT, PATCH, and DELETE.
methods = {"GET": "read", "POST": "create", "PUT": "replace", "DELETE": "remove"}
for method, meaning in methods.items():
    print(f"{method}: {meaning}")

# Expected output:
# GET: read
# POST: create
# PUT: replace
# DELETE: remove
