# ==================================================
# QUESTION 01: Why do we use try/except blocks in Python?
# ==================================================

# SOLUTION:
# They let the program handle bad data without crashing.
try:
    amount = int("abc")
except ValueError:
    print("That is not a valid integer.")
finally:
    print("Cleanup complete.")

# QUESTION 02: How do we validate an order quantity safely?
# ==================================================

# SOLUTION:
quantity = 0
try:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
except ValueError as exc:
    print(exc)

# Expected output:
# That is not a valid integer.
# Cleanup complete.
# Quantity must be greater than zero.
