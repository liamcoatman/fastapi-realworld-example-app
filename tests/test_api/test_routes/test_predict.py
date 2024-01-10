from uuid import UUID
from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_predict(app: FastAPI, model_prediction_uid: UUID):
    with TestClient(app) as client:
        response = client.post(app.url_path_for("predict"), json={"features": [-4, 1, 0, 10, -2, 1]})
    assert response.status_code == 200
    assert response.json() == {
        'modelGroup': 'model_group',
        'modelName': 'model_name',
        'modelPredictionUid': str(model_prediction_uid),
        'modelVersion': 1,
        'result': [0, 1, 0, 1, 0, 1],
    }
