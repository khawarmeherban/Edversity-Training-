# ==================================================
# QUESTION 01: How do we create a project with uv and add a dependency?
# ==================================================

# SOLUTION:
# Typical commands:
# uv init my-project
# cd my-project
# uv add requests
# uv run python app.py
#
# For a demonstration, we can show what the files would look like.
from pathlib import Path

config = {
    "project": "learn-python",
    "requires-python": ">=3.10",
    "dependencies": ["requests"],
}

print(config)
print(Path("pyproject.toml").exists())

# Expected output:
# {'project': 'learn-python', 'requires-python': '>=3.10', 'dependencies': ['requests']}
# False
