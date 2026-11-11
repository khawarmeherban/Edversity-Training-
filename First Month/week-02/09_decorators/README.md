# ==================================================
# QUESTION 01: What is a decorator and why is it helpful?
# ==================================================

# SOLUTION:
# A decorator wraps a function and adds functionality without changing
# the function body itself.
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Bilal"))

# Expected output:
# Calling greet
# Hello, Bilal!
