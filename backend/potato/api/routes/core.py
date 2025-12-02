from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from typing import Final
import asyncio

from potato.models import ServiceSettings
from potato.api.models import ServiceStatus
from potato.logs import LOG_QUEUE
from potato.storage.db import StorageDB

API_MODULE_ID: Final[str] = "core"


class CoreAPI:
    def __init__(self, settings: ServiceSettings, storage_db: StorageDB) -> None:
        self._settings = settings
        self._storage_db = storage_db

        self._router = APIRouter()
        self._init_routes()

    @property
    def router(self) -> APIRouter:
        return self._router

    def _init_routes(self) -> None:
        self.router.add_api_route(
            "/status",
            self.get_status,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/logs",
            self.stream_logs,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

    async def get_status(self) -> ServiceStatus:
        return ServiceStatus(
            settings=self._settings,
            storage_path=str(self._storage_db.path),
            db_debug=self._storage_db.debug,
            total_recipes=self._storage_db.total_recipes,
        )

    async def stream_logs(self):
        async def log_steam():
            while True:
                try:
                    # attempt to pull a log message without blocking
                    log_message = LOG_QUEUE.get_nowait()
                    yield f"{log_message}\n"
                except Exception:
                    # if queue is empty, yield nothing and wait briefly
                    await asyncio.sleep(0.1)

        return StreamingResponse(log_steam(), media_type="text/event-stream")
