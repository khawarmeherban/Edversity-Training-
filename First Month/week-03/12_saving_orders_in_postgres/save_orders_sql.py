# ==================================================
# QUESTION 01: How do we prepare an insert for an order record?
# ==================================================

# SOLUTION:
insert_sql = """
INSERT INTO orders (customer_name, item, quantity, total, status)
VALUES ('Noor Foods', 'Rice', 2, 520, 'pending');
"""
print(insert_sql)

# Expected output:
# INSERT INTO orders ...
