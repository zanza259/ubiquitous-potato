from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from prometheus_fastapi_instrumentator import Instrumentator
from potato.logs import REGISTRY

from potato.models import ServiceSettings
from potato.api.routes.core import CoreAPI
from potato.api.routes.user import UserAPI
from potato.api.routes.group import GroupAPI
from potato.api.routes.site import SiteAPI
from potato.api.routes.recipe import RecipeAPI
from potato.storage.db import StorageDB

logger = logging.getLogger(__name__)


def build_app(settings: ServiceSettings, storage_db: StorageDB) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # run at startup
        app.state.settings = settings
        app.state.storage = storage_db

        # expose the prometheus metrics endpoint
        insturmentator.expose(app, include_in_schema=False, should_gzip=True)

        logger.info("FastAPI surface startup complete (uvicorn)")

        yield

        # run at shutdown
        logger.info("FastAPI surface shutdown complete (uvicorn)")
        print("Shutting down uvicorn server")

    # setup api routes
    core_api = CoreAPI(settings=settings, storage_db=storage_db)
    recipe_api = RecipeAPI(settings=settings, storage_db=storage_db)
    group_api = GroupAPI(settings=settings)
    site_api = SiteAPI(settings=settings)
    user_api = UserAPI(settings=settings)

    # build out fast api application
    app = FastAPI(
        lifespan=lifespan,
        title=settings.service_id,
        version="0.1.0",  # TODO: link to poetry
    )

    insturmentator = Instrumentator(
        excluded_handlers=["/metrics"],  # we will expose metrics endpoint ourselves
        registry=REGISTRY,
    )

    insturmentator.instrument(
        app,
        metric_namespace=settings.service_id.replace(
            "-", "_"
        ),  # prometheus metric namespace must not have dashes
    )

    app.include_router(core_api.router)
    app.include_router(recipe_api.router)
    app.include_router(group_api.router)
    app.include_router(site_api.router)
    app.include_router(user_api.router)

    # setup CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
