# ==================================================
# QUESTION 01: How do we model the update and delete flow for order records?
# ==================================================

# SOLUTION:
orders = {1: {"customer_name": "Noor Foods", "total": 500}}

order_id = 1
orders[order_id]["total"] = 600
print(orders)

del orders[order_id]
print(orders)

# Expected output:
# {1: {'customer_name': 'Noor Foods', 'total': 600}}
# {}
