from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_health(app: FastAPI):
    with TestClient(app) as client:
        response = client.get(app.url_path_for("health"))
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
