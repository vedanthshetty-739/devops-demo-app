# test/test_main.py
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5

    response = client.post("/add", json={"a": -1, "b": 1})
    assert response.status_code == 200
    assert response.json()["result"] == 0

def test_subtract():
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 2

    response = client.post("/subtract", json={"a": 0, "b": 2})
    assert response.status_code == 200
    assert response.json()["result"] == -2
