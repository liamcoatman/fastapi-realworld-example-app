from functools import lru_cache

from app.core.settings.app import AppSettings
from app.core.settings.base import AppEnvTypes, BaseAppSettings
from app.core.settings.demo import DemoAppSettings
from app.core.settings.prod import ProdAppSettings


environments: dict[AppEnvTypes, type[AppSettings]] = {
    AppEnvTypes.demo: DemoAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()  # pyright: ignore
