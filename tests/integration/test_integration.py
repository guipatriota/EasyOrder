from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_criar_obter_atualizar_deletar_ordem():
    # 1. Criar uma nova ordem
    nova_ordem = {
        "id": 10,
        "customer_name": "Maria",
        "items": [
            {"product_id": 1, "product_name": "Caderno", "quantity": 2, "price": 10.0}
        ]
    }
    response_post = client.post("/orders", json=nova_ordem)
    assert response_post.status_code == 200
    assert response_post.json()["ordem"]["customer_name"] == "Maria"

    # 2. Obter a ordem criada
    response_get = client.get("/orders/10")
    assert response_get.status_code == 200
    assert response_get.json()["id"] == 10

    # 3. Atualizar status da ordem
    response_put = client.put("/orders/10/status?status=closed")
    assert response_put.status_code == 200
    assert response_put.json()["ordem"]["status"] == "closed"

    # 4. Deletar a ordem
    response_delete = client.delete("/orders/10")
    assert response_delete.status_code == 200
    assert response_delete.json()["ordem"]["id"] == 10

    # 5. Verificar que a ordem não existe mais
    response_get_404 = client.get("/orders/10")
    assert response_get_404.status_code == 404
