# ==================================================
# QUESTION 01: How do we write a basic API test with TestClient?
# ==================================================

# SOLUTION:
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get('/health')
def health() -> dict[str, str]:
    return {"status": "ok"}

client = TestClient(app)
response = client.get('/health')
print(response.status_code)
print(response.json())

# Expected output:
# 200
# {'status': 'ok'}
