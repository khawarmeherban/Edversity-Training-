# ==================================================
# QUESTION 01: How do we use Python's standard library of dates?
# ==================================================

# SOLUTION:
from datetime import date, timedelta

today = date.today()
next_week = today + timedelta(days=7)
print(today)
print(next_week)

# QUESTION 02: How do we create an enum for allowed order states?
# ==================================================

# SOLUTION:
from enum import StrEnum, auto

class OrderState(StrEnum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

print(OrderState.PENDING)
print(OrderState.SHIPPED == "shipped")

# Expected output:
# 2026-11-11
# 2026-11-18
# pending
# True
