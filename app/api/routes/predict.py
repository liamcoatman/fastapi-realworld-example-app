from gettext import dpgettext
from typing import Annotated, reveal_type
from uuid import UUID
from annotated_types import Len
from fastapi import APIRouter, Depends
from loguru import logger
from app.api.dependencies import generate_uuid
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings
from app.models.schemas.predict import PredictRequest, PredictResponse
from app.resources import ml_models
import numpy as np

type ModelInputType = Annotated[list[int], Len(6, 6)]
type ModelOutputType = Annotated[list[int], Len(6, 6)]

router = APIRouter()

@router.post(
    "/",
    name="predict", 
    tags=["predict"], 
    summary="Send prediction request to model",
)
async def predict(
    request: PredictRequest[ModelInputType], 
    model_prediction_uid: Annotated[UUID, Depends(generate_uuid)],
    settings: Annotated[AppSettings, Depends(get_app_settings)]
) -> PredictResponse[ModelOutputType]:
    features = np.array(request.model_input).reshape(-1, 1)
    result = ml_models[settings.model_name].predict(features)
    return PredictResponse(
        model_group="model_group",
        model_name="model_name",
        model_version=1,
        model_prediction_uid=model_prediction_uid,
        result=result,
    )
