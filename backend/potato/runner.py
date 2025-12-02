import argparse
import asyncio
import logging
import uvicorn
from pathlib import Path
from potato.logs import QueueHandler, LOG_QUEUE
from potato.api.app import build_app
from potato.models import ServiceSettings
from potato.storage.db import StorageDB

# setup root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

queue_handler = QueueHandler(log_queue=LOG_QUEUE)
queue_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

root_logger.addHandler(queue_handler)

# setup module logger
logger = logging.getLogger(__name__)


class Runner:
    def __init__(self, settings: ServiceSettings) -> None:
        self._settings = settings

    @property
    def settings(self) -> ServiceSettings:
        return self._settings

    async def run(self) -> None:
        logger.info(f"Starting backend with database at {self._settings.db_path}")

        storage_db = StorageDB(
            db_path=self._settings.db_path,
            debug=self._settings.debug,
        )

        fast_api_app = build_app(
            settings=self._settings,
            storage_db=storage_db,
        )

        config = uvicorn.Config(
            app=fast_api_app,
            port=self._settings.port,
            log_level="info",  # make sure uvicorn doesn't override the logging level if we set it elsewhere
            log_config=None,  # make sure that uvicorn doesn't override the global logger configuration
            access_log=False,  # disable access log to prevent prometheus metric harvesting spamming logs
            lifespan="on",  # lifespan to ensure startup/shutdown events are handled
            host="0.0.0.0",
        )

        server = uvicorn.Server(config=config)

        try:
            await server.serve()
        finally:
            logger.info("Shutting down backend")
            await server.shutdown()
            print("Backend shutdown complete")


def build_arg_parser():
    parser = argparse.ArgumentParser(description="Recipe Management Backend")

    parser.add_argument(
        "--db",
        type=Path,
        default=Path.home() / "recipes.db",
        help="Path to the designated sqlite database file.",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8090,
        help="Port to run the backend server on.",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging.",
    )

    return parser


def main():
    args = build_arg_parser().parse_args()

    settings = ServiceSettings(
        port=args.port,
        db_path=args.db.resolve(),
        debug=args.debug,
    )

    if settings.debug:
        root_logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        root_logger.addHandler(console_handler)

    runner = Runner(settings=settings)
    asyncio.run(runner.run())


if __name__ == "__main__":
    main()
