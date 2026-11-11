# ==================================================
# QUESTION 01: What basic VS Code settings help Python development?
# ==================================================

# SOLUTION:
settings = {
    "python.analysis.typeCheckingMode": "basic",
    "python.testing.pytestEnabled": True,
    "editor.formatOnSave": True,
    "files.exclude": {"**/__pycache__": True},
}

for key, value in settings.items():
    print(f"{key}: {value}")

# Expected output:
# python.analysis.typeCheckingMode: basic
# python.testing.pytestEnabled: True
# editor.formatOnSave: True
# files.exclude: {'**/__pycache__': True}
