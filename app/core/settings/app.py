import logging
import sys
from typing import Any
from pydantic_settings import SettingsConfigDict

import sentry_sdk

from loguru import logger

from app.core.logging import InterceptHandler
from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "ML model serving example application"
    version: str = "0.0.0"

    api_prefix: str = "/api"

    logging_level: int = logging.INFO
    loggers: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    model_name: str
    model_path: str
    # route, schema?

    # sentry_dsn: str
    # sentry_environment: str
    # sentry_tags_cluster: str
    # sentry_tags_tenant: str

    # build_number: str

    model_config = SettingsConfigDict(protected_namespaces=("settings_",))

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])

    # def configure_sentry(self) -> None:
    #     # TODO: Filter out suppressed exceptions
    #     sentry_sdk.init(
    #         dsn=self.sentry_dsn,
    #         environment=self.sentry_environment,
    #         release=self.build_number,
    #     )

    #     sentry_sdk.set_tag("application", self.title)
    #     sentry_sdk.set_tag("cluster", self.sentry_tags_cluster)
    #     sentry_sdk.set_tag("tenant", self.sentry_tags_tenant)
