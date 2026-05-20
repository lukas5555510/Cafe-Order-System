from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_world_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert json_data["data"] == {"message": "Hello World"}
