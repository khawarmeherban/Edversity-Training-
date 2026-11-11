# ==================================================
# QUESTION 01: How can we write a pytest test for a simple helper function?
# ==================================================

# SOLUTION:

def is_even(value: int) -> bool:
    return value % 2 == 0


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

print("pytest example ready")

# To run:
# pytest -q
#
# Expected output:
# 2 passed
