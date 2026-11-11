# ==================================================
# QUESTION 01: How do we use SQL to query an orders table?
# ==================================================

# SOLUTION:
query = "SELECT customer_name, total FROM orders WHERE total > 500;"
print(query)

# Expected output:
# SELECT customer_name, total FROM orders WHERE total > 500;
