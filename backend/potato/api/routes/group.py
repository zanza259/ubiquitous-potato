from fastapi import APIRouter
from typing import Final

from potato.api.models import unimplemented
from potato.models import ServiceSettings

API_MODULE_ID: Final[str] = "group"


class GroupAPI:
    def __init__(self, settings: ServiceSettings) -> None:
        self._settings = settings

        self._router = APIRouter()
        self._init_routes()

    @property
    def router(self) -> APIRouter:
        return self._router

    def _init_routes(self) -> None:
        self.router.add_api_route(
            "/groups",
            unimplemented,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/group",
            unimplemented,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/group/{group_id}",
            unimplemented,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/group/{group_id}",
            unimplemented,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/group/{group_id}",
            unimplemented,
            methods=["DELETE"],
            tags=[API_MODULE_ID],
        )
