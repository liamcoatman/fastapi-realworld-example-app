from uuid import UUID
import pytest
from fastapi import FastAPI

from app.api.dependencies import generate_uuid

@pytest.fixture
def model_prediction_uid() -> UUID:
    return UUID("579e87ef-fdfe-4eb7-81d1-e477acf1a7b4")


@pytest.fixture
def app(model_prediction_uid) -> FastAPI:
    from app.main import get_application
    app = get_application()
    app.dependency_overrides[generate_uuid] = lambda: model_prediction_uid
    return app
