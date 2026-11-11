# ==================================================
# QUESTION 01: Why do we use type hints in Python?
# ==================================================

# SOLUTION:
# Type hints make the input and output of functions clearer and improve
# editor support and static checks.
from typing import Iterable


def total_amount(items: Iterable[int]) -> int:
    return sum(items)

print(total_amount([10, 20, 30]))

# Expected output:
# 60
