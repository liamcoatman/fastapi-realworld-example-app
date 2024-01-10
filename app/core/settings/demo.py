import logging

from app.core.settings.app import AppSettings


class DemoAppSettings(AppSettings):
    debug: bool = True
    logging_level: int = logging.DEBUG
    model_path: str = "/workspaces/fastapi-realworld-example-app/mlruns/0/b841bd834cd3411eba9cbf0064686e3b/artifacts/model/"
