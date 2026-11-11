# ==================================================
# QUESTION 01: How do we implement a timing decorator?
# ==================================================

# SOLUTION:
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def total(items):
    return sum(items)

print(total([2, 4, 6]))

# Expected output:
# 12
# total took 0.000x seconds
