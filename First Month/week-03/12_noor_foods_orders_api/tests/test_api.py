import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.database import get_session
from app.main import app


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    def override_get_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def create_order_payload(**overrides):
    payload = {
        "customer_name": "Noor Foods",
        "item": "Fresh rice",
        "quantity": 2,
        "total": 520.0,
        "status": "pending",
    }
    payload.update(overrides)
    return payload


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_orders_returns_empty_list(client):
    response = client.get("/orders")
    assert response.status_code == 200
    assert response.json() == []


def test_create_order_success(client):
    payload = create_order_payload()
    response = client.post("/orders", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["customer_name"] == "Noor Foods"
    assert data["item"] == "Fresh rice"
    assert data["status"] == "pending"


def test_list_orders_with_customer_filter(client):
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods"))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Tea Pack"))

    response = client.get("/orders", params={"customer": "noor foods"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["customer_name"] == "Noor Foods"


def test_list_orders_with_status_filter(client):
    client.post("/orders", json=create_order_payload(status="pending"))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Chips", status="delivered"))

    response = client.get("/orders", params={"status": "delivered"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["status"] == "delivered"


def test_list_orders_with_min_total_filter(client):
    client.post("/orders", json=create_order_payload(total=250.0))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Soda", total=1200.0))

    response = client.get("/orders", params={"min_total": 800})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["customer_name"] == "Bilal Traders"


def test_list_orders_with_combined_filters(client):
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", item="Rice", total=300.0, status="pending"))
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", item="Milk", total=1200.0, status="delivered"))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Tea", total=1200.0, status="delivered"))

    response = client.get("/orders", params={"customer": "Noor Foods", "status": "delivered", "min_total": 1000})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["item"] == "Milk"


def test_get_customer_orders_route(client):
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", item="Rice"))
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", item="Flour"))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Tea"))

    response = client.get("/customers/noor foods/orders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert {order["item"] for order in data} == {"Rice", "Flour"}


def test_summary_endpoint(client):
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", total=200.0))
    client.post("/orders", json=create_order_payload(customer_name="Bilal Traders", item="Beans", total=800.0))
    client.post("/orders", json=create_order_payload(customer_name="Noor Foods", item="Milk", total=600.0))

    response = client.get("/summary")
    assert response.status_code == 200
    data = response.json()
    assert data["total_orders"] == 3
    assert data["total_revenue"] == 1600.0
    assert data["average_order_value"] == 533.33
    assert data["customers_served"] == 2


def test_update_order(client):
    created = client.post("/orders", json=create_order_payload(item="Rice", total=100.0)).json()
    response = client.put(f"/orders/{created['id']}", json={"customer_name": "Bilal Traders", "item": "Rice", "quantity": 3, "total": 300.0, "status": "processing"})
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Bilal Traders"
    assert data["quantity"] == 3
    assert data["status"] == "processing"


def test_delete_order(client):
    created = client.post("/orders", json=create_order_payload(item="Tea", total=75.0)).json()
    response = client.delete(f"/orders/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]

    later = client.get("/orders")
    assert later.json() == []


def test_invalid_status_returns_400(client):
    response = client.get("/orders", params={"status": "unknown"})
    assert response.status_code == 400
    assert "status must be one of" in response.json()["detail"]


def test_invalid_total_raises_validation_error(client):
    payload = create_order_payload(total=-10)
    response = client.post("/orders", json=payload)
    assert response.status_code == 422


def test_order_not_found(client):
    response = client.put("/orders/999", json=create_order_payload())
    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"

    delete_response = client.delete("/orders/999")
    assert delete_response.status_code == 404


def test_blank_customer_name_is_rejected(client):
    payload = create_order_payload(customer_name="   ")
    response = client.post("/orders", json=payload)
    assert response.status_code == 422


def test_create_order_uses_case_insensitive_status(client):
    payload = create_order_payload(status="DELIVERED")
    response = client.post("/orders", json=payload)
    assert response.status_code == 201
    assert response.json()["status"] == "delivered"
