from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def validation_exception_handler(
    _: Request,
    exc: RequestValidationError | ValidationError,
) -> JSONResponse:
    return JSONResponse(
        content={"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )
