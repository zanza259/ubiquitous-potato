from pydantic import BaseModel
from potato.models import ServiceSettings


class BasicResponse(BaseModel):
    message: str


class ServiceStatus(BaseModel):
    settings: ServiceSettings
    storage_path: str
    db_debug: bool
    total_recipes: int


async def unimplemented():
    return BasicResponse(message="This endpoint is not yet implemented.")
