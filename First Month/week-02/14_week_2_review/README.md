# ==================================================
# QUESTION 01: How do the learning goals from Week 2 fit together?
# ==================================================

# SOLUTION:
# The week combines tooling, project setup, data handling, classes,
# validation, and testing. Together they create a solid Python workflow
# for real-world engineering work.
summary = {
    "tooling": "Python, uv, VS Code",
    "data": "collections, mutability, exceptions",
    "design": "classes, decorators, type hints",
    "quality": "mypy, pydantic, pytest",
}
for key, value in summary.items():
    print(f"{key}: {value}")

# Expected output:
# tooling: Python, uv, VS Code
# data: collections, mutability, exceptions
# design: classes, decorators, type hints
# quality: mypy, pydantic, pytest
