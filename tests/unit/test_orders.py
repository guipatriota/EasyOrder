"""Testes unitários das rotas de pedidos da EasyOrder.

Cobre o endpoint raiz e o fluxo básico de criação e listagem de pedidos.
"""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root():
    """Valida o endpoint raiz.

    Verifica que a resposta tem status 200 e contém mensagem de boas-vindas.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Bem-vindo" in response.json()["mensagem"]


def test_create_and_list_order():
    """Cria um pedido e valida a listagem.

    Envia um POST para criar um pedido e confirma que ele aparece na listagem.
    """
    order = {
        "id": 1,
        "customer_name": "João",
        "items": [
            {
                "product_id": 101,
                "product_name": "Caneta",
                "quantity": 2,
                "price": 1.5,
            }
        ],
    }
    resp_post = client.post("/orders", json=order)
    assert resp_post.status_code == 200

    resp_list = client.get("/orders")
    assert resp_list.status_code == 200
    assert len(resp_list.json()) == 1
