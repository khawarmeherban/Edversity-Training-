# ==================================================
# QUESTION 01: How can we safely divide two numbers?
# ==================================================

# SOLUTION:
values = [12, 0, 8]
for number in values:
    try:
        print(f"12 / {number} = {12 / number}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# Expected output:
# 12 / 12 = 1.0
# Cannot divide by zero.
# 12 / 8 = 1.5
