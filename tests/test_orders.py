
import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client():
    app = create_app()

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_order(client):
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Andini",
            "phone": "081234567890",
            "weight_kg": 4.5,
            "service_type": "regular",
            "notes": "Pisahkan pakaian putih",
        },
    )

    assert response.status_code == 201
    return response.json()


def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_create_order(client):
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Andini",
            "phone": "081234567890",
            "weight_kg": 4.5,
            "service_type": "regular",
        },
    )

    assert response.status_code == 201
    assert response.json()["total_price"] == 31500
    assert response.json()["status"] == "pending"


def test_express_price(client):
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Andini",
            "phone": "081234567890",
            "weight_kg": 2,
            "service_type": "express",
        },
    )

    assert response.status_code == 201
    assert response.json()["price_per_kg"] == 12000
    assert response.json()["total_price"] == 24000


def test_get_all_orders(client, sample_order):
    response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == sample_order["id"]


def test_get_order_by_id(client, sample_order):
    order_id = sample_order["id"]
    response = client.get(f"/api/orders/{order_id}")

    assert response.status_code == 200
    assert response.json()["customer_name"] == "Andini"


def test_update_order_status(client, sample_order):
    order_id = sample_order["id"]

    response = client.patch(
        f"/api/orders/{order_id}/status",
        json={"status": "washing"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "washing"


def test_delete_order(client, sample_order):
    order_id = sample_order["id"]

    response = client.delete(f"/api/orders/{order_id}")
    assert response.status_code == 204

    response = client.get(f"/api/orders/{order_id}")
    assert response.status_code == 404


def test_invalid_weight(client):
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Andini",
            "phone": "081234567890",
            "weight_kg": 0,
            "service_type": "regular",
        },
    )

    assert response.status_code == 422


def test_invalid_service_type(client):
    response = client.post(
        "/api/orders",
        json={
            "customer_name": "Andini",
            "phone": "081234567890",
            "weight_kg": 2,
            "service_type": "superfast",
        },
    )

    assert response.status_code == 422


def test_invalid_order_status(client, sample_order):
    response = client.patch(
        f"/api/orders/{sample_order['id']}/status",
        json={"status": "lost"},
    )

    assert response.status_code == 422


def test_order_not_found(client):
    response = client.get("/api/orders/999999")

    assert response.status_code == 404


def test_delete_order_not_found(client):
    response = client.delete("/api/orders/999999")

    assert response.status_code == 404
