from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bem-vindo" in response.json()["mensagem"]

def test_create_and_list_order():
    order = {
        "id": 1,
        "customer_name": "João",
        "items": [
            {"product_id": 101, "product_name": "Caneta", "quantity": 2, "price": 1.5}
        ]
    }
    resp_post = client.post("/orders", json=order)
    assert resp_post.status_code == 200

    resp_list = client.get("/orders")
    assert resp_list.status_code == 200
    assert len(resp_list.json()) == 1
