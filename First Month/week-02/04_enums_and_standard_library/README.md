# ==================================================
# QUESTION 01: What is an enum and why is it useful?
# ==================================================

# SOLUTION:
# Enums are a fixed set of named values. They reduce typos and make
# code easier to read when values are limited.
from enum import Enum, auto

class PaymentMethod(Enum):
    CASH = auto()
    CARD = auto()
    BANK_TRANSFER = auto()

for method in PaymentMethod:
    print(method.name, method.value)

# Expected output:
# CASH 1
# CARD 2
# BANK_TRANSFER 3
