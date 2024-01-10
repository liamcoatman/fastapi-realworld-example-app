from fastapi import APIRouter

from app.api.routes import predict, health

router = APIRouter()
router.include_router(predict.router, prefix="/predict")
router.include_router(health.router, prefix="/health")

POST "/v1/models/{model_name}/versions/{model_version}/infer"

