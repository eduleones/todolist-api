from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlmodel import Session, SQLModel, create_engine


class Database:
    def __init__(self, db_url: str):
        self._engine = create_engine(db_url)
        self._session_factory = Session(self._engine)

    def create_database(self):
        SQLModel.metadata.create_all(self._engine)

    def get_tables(self):
        return SQLModel.metadata.tables.keys()

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
