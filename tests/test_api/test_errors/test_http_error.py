from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_404_NOT_FOUND


def test_validation_error_format(app: FastAPI):
    with TestClient(base_url="http://testserver", app=app) as client:
        response = client.get("/wrong_path/asd")

    assert response.status_code == HTTP_404_NOT_FOUND
    assert "errors" in response.json()