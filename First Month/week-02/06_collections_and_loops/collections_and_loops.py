# ==================================================
# QUESTION 01: How do we build a list of order totals with a loop?
# ==================================================

# SOLUTION:
orders = [450, 1200, 200, 900]
order_totals = []
for total in orders:
    if total >= 500:
        order_totals.append(total)
print(order_totals)

# QUESTION 02: How do we loop over a dictionary and calculate a total?
# ==================================================

# SOLUTION:
products = {"rice": 120, "oil": 200, "tea": 80}
product_total = 0
for price in products.values():
    product_total += price
print(product_total)

# Expected output:
# [1200]
# 400
