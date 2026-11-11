# ==================================================
# QUESTION 01: How do we create a minimal FastAPI app?
# ==================================================

# SOLUTION:
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


print("FastAPI app initialized")
