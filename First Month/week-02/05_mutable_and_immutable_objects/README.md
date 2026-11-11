# ==================================================
# QUESTION 01: What is the difference between mutable and immutable objects?
# ==================================================

# SOLUTION:
# Mutable objects can be changed after creation. Immutable objects cannot.
# A list is mutable, while a string is immutable.
prices = [100, 200, 300]
prices.append(400)
print(prices)

name = "Noor"
# name[0] = "B"  # This would fail; strings are immutable.
print(name.upper())

# Expected output:
# [100, 200, 300, 400]
# NOOR
