# ==================================================
# QUESTION 01: Why should VS Code be configured for Python projects?
# ==================================================

# SOLUTION:
# VS Code should use the selected interpreter, auto-formatting, and
# built-in testing support to keep work consistent.
settings = {
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
    "python.testing.pytestEnabled": True,
    "editor.formatOnSave": True,
}
print(settings)

# Expected output:
# {'python.defaultInterpreterPath': '.venv\\Scripts\\python.exe',
#  'python.testing.pytestEnabled': True,
#  'editor.formatOnSave': True}
