# ==================================================
# QUESTION 01: Why do we test code with pytest?
# ==================================================

# SOLUTION:
# pytest is simple to read, fast to run, and good for verifying edge cases.
# Example tests:
#
# def test_addition():
#     assert 2 + 2 == 4

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))

# Expected output:
# 5
