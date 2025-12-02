import logging
from queue import Queue
from prometheus_client import CollectorRegistry
from typing import Final

REGISTRY: Final[CollectorRegistry] = CollectorRegistry(auto_describe=True)
LOG_QUEUE: Final[Queue] = Queue(maxsize=100)


class QueueHandler(logging.Handler):
    def __init__(self, log_queue: Queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record: logging.LogRecord) -> None:
        if self.log_queue.full():
            try:
                self.log_queue.get_nowait()
            except Queue.Empty:
                pass

        self.log_queue.put(self.format(record))
