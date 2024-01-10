from typing import Annotated
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from annotated_types import Len


class PredictRequest[T](BaseModel):
    model_input: T

    # model_config = ConfigDict(
    #     json_schema_extra={
    #         "examples": [{"features": [-4, 1, 0, 10, -2, 1]}]
    #     }
    # )
    

class PredictResponse[T](BaseModel):    
    model_group: str
    model_name: str
    model_version: int
    model_prediction_uid: UUID
    model_output: T

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True, 
        protected_namespaces=(),
    )
