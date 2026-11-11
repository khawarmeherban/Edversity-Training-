# ==================================================
# QUESTION 01: How can you confirm Python and uv are installed
# and available in the environment?
# ==================================================

# SOLUTION:
# We can check the interpreter version and whether the uv command
# is present in the PATH.
import shutil
import sys

print(sys.version)
print("uv installed:", shutil.which("uv") is not None)

# Expected output:
# Python 3.x.x
# uv installed: True
