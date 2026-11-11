# ==================================================
# QUESTION 01: How can we confirm Python is installed and report
# the version?
# ==================================================

# SOLUTION:
import sys

python_version = sys.version.split()[0]
print(f"Python version: {python_version}")

# QUESTION 02: How do we check whether uv is available on this machine?
# ==================================================

# SOLUTION:
import shutil

print("uv available:", shutil.which("uv") is not None)

# QUESTION 03: How can we make a small environment health report?
# ==================================================

# SOLUTION:
print("Environment ready:", sys.version_info >= (3, 10))

# Expected output:
# Python version: 3.13.x
# uv available: True
# Environment ready: True
