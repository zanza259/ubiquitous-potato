from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session


class StorageDB:
    def __init__(self, db_path: Path, debug: bool = False):
        self._db_path = db_path
        self._debug = debug

        self._engine = create_engine(f"sqlite:///{self._db_path}", echo=self._debug)
        self._root_session = sessionmaker(bind=self._engine)

    @property
    def path(self) -> Path:
        return self._db_path

    @property
    def debug(self) -> bool:
        return self._debug

    @property
    def total_recipes(self) -> int:
        with self.new_session() as session:
            result = session.execute(text("SELECT COUNT(*) FROM potato_recipe"))
            count = result.scalar_one()
            return count

    def new_session(self) -> Session:
        return self._root_session()
