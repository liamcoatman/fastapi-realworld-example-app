from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    model_path: str = "/workspaces/fastapi-realworld-example-app/mlruns/0/b841bd834cd3411eba9cbf0064686e3b/artifacts/model/"

