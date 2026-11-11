# ==================================================
# QUESTION 01: How can we prepare a file for mypy checks?
# ==================================================

# SOLUTION:
from typing import Sequence


def count_values(items: Sequence[int]) -> int:
    return len(items)

print(count_values([1, 2, 3]))

# Expected output:
# 3
