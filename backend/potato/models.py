from pydantic import BaseModel
from pathlib import Path


class ServiceSettings(BaseModel):
    service_id: str = "recipe-manager-backend"
    port: int
    db_path: Path
    debug: bool
