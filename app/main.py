from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
import mlflow

from app.api.errors.http_error import http_exception_handler
from app.api.errors.validation_error import validation_exception_handler
from app.api.middleware import CorrelationIdMiddleware
from app.api.routes.api import router as api_router
from app.core.config import get_app_settings
from app.resources import ml_models


class Model:
    def load_model(self):
        ...

    def predict(self):
        ...



def get_application() -> FastAPI:    
    settings = get_app_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        ml_models[settings.model_name] = mlflow.pyfunc.load_model(settings.model_path)
        yield
        ml_models.clear()

    settings.configure_logging()
    # settings.configure_sentry()
    
    application = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)

    application.add_middleware(CorrelationIdMiddleware)

    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(RequestValidationError, validation_exception_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()
