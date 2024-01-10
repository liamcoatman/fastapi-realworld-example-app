from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    demo = "demo"
    prod = "prod"
    

class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.prod
