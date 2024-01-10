from fastapi import APIRouter

from app.models.schemas.health import HealthResponse


router = APIRouter()

    
@router.get(
    "/",
    name="health",
    tags=["health"], 
    summary="Check health of server", 
)
async def health() -> HealthResponse:
    return HealthResponse()
