from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from products_api import main


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setattr(main, "products", deepcopy(main.initial_products))
    monkeypatch.setattr(main, "next_product_number", 105)
    return TestClient(main.app)


def create_product(
    client: TestClient,
    *,
    name: str = "Chakki atta 10kg",
    price: int = 1800,
    category: str = "flour",
    in_stock: int = 0,
) -> dict[str, object]:
    response = client.post(
        "/products",
        json={
            "name": name,
            "price": price,
            "category": category,
            "in_stock": in_stock,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_products_starts_with_four_products(client: TestClient) -> None:
    response = client.get("/products")
    assert response.status_code == 200
    assert [product["id"] for product in response.json()] == ["P101", "P102", "P103", "P104"]


def test_list_products_combines_filters_and_limit(client: TestClient) -> None:
    response = client.get(
        "/products",
        params={"category": "rice", "max_price": 3000, "limit": 1},
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "P101",
            "name": "Basmati rice 5kg",
            "price": 2400,
            "category": "rice",
            "in_stock": 40,
        }
    ]


def test_list_products_rejects_unknown_category(client: TestClient) -> None:
    response = client.get("/products", params={"category": "sugar"})
    assert response.status_code == 422


def test_get_product_by_id(client: TestClient) -> None:
    response = client.get("/products/P103")
    assert response.status_code == 200
    assert response.json()["name"] == "Red chilli powder 200g"


def test_get_missing_product_returns_named_404(client: TestClient) -> None:
    response = client.get("/products/P999")
    assert response.status_code == 404
    assert "P999" in response.json()["detail"]


def test_create_product_uses_next_id_and_default_stock(client: TestClient) -> None:
    response = client.post(
        "/products",
        json={"name": "Chakki atta 10kg", "price": 1800, "category": "flour"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": "P105",
        "name": "Chakki atta 10kg",
        "price": 1800,
        "category": "flour",
        "in_stock": 0,
    }


@pytest.mark.parametrize(
    "payload",
    [
        {"name": "A", "price": 100, "category": "flour"},
        {"name": "Rice", "price": 0, "category": "rice"},
        {"name": "Rice", "price": 100, "category": "sugar"},
        {"name": "Rice", "price": 100, "category": "rice", "in_stock": -1},
    ],
)
def test_create_product_rejects_invalid_data(
    client: TestClient,
    payload: dict[str, object],
) -> None:
    response = client.post("/products", json=payload)
    assert response.status_code == 422


def test_create_product_trims_name(client: TestClient) -> None:
    product = create_product(client, name="  Chakki atta 10kg  ")
    assert product["name"] == "Chakki atta 10kg"


def test_patch_changes_only_the_supplied_fields(client: TestClient) -> None:
    product = create_product(client, name="Chilli powder", category="spices", in_stock=20)
    response = client.patch(f"/products/{product['id']}", json={"price": 350})
    assert response.status_code == 200
    assert response.json() == {
        "id": product["id"],
        "name": "Chilli powder",
        "price": 350,
        "category": "spices",
        "in_stock": 20,
    }


def test_patch_rejects_negative_stock_without_changing_product(client: TestClient) -> None:
    product = create_product(client, in_stock=5)
    response = client.patch(f"/products/{product['id']}", json={"in_stock": -5})
    assert response.status_code == 422
    assert client.get(f"/products/{product['id']}").json()["in_stock"] == 5


def test_patch_rejects_explicit_null(client: TestClient) -> None:
    product = create_product(client)
    response = client.patch(f"/products/{product['id']}", json={"price": None})
    assert response.status_code == 422


def test_patch_missing_product_returns_named_404(client: TestClient) -> None:
    response = client.patch("/products/P999", json={"price": 350})
    assert response.status_code == 404
    assert "P999" in response.json()["detail"]


def test_delete_rejects_products_with_stock(client: TestClient) -> None:
    product = create_product(client, in_stock=3)
    response = client.delete(f"/products/{product['id']}")
    assert response.status_code == 409
    assert client.get(f"/products/{product['id']}").status_code == 200


def test_delete_removes_zero_stock_product(client: TestClient) -> None:
    product = create_product(client)
    response = client.delete(f"/products/{product['id']}")
    assert response.status_code == 204
    assert response.content == b""
    assert client.get(f"/products/{product['id']}").status_code == 404


def test_delete_missing_product_returns_named_404(client: TestClient) -> None:
    response = client.delete("/products/P999")
    assert response.status_code == 404
    assert "P999" in response.json()["detail"]


def test_deleted_product_id_is_never_reused(client: TestClient) -> None:
    first = create_product(client)
    assert client.delete(f"/products/{first['id']}").status_code == 204
    second = create_product(client, name="New flour")
    assert second["id"] == "P106"


def test_summary_matches_starting_inventory(client: TestClient) -> None:
    response = client.get("/summary")
    assert response.status_code == 200
    assert response.json() == {
        "product_count": 4,
        "stock_value": 203400,
        "by_category": {"rice": 2, "oil": 1, "spices": 1},
    }
