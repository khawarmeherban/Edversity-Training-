# ==================================================
# QUESTION 01: How can we use lists, tuples, sets, and dictionaries together?
# ==================================================

# SOLUTION:
stock = {"rice": 10, "oil": 5, "sugar": 2}
items = ["rice", "oil", "tea"]
seen = set(items)
print(stock)
print(seen)

# QUESTION 02: How do loops help us process collections?
# ==================================================

# SOLUTION:
for product, quantity in stock.items():
    print(f"{product}: {quantity}")

# Expected output:
# {'rice': 10, 'oil': 5, 'sugar': 2}
# {'rice', 'oil', 'tea'}
# rice: 10
# oil: 5
# sugar: 2
