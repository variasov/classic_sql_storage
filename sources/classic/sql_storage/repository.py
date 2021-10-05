from sqlalchemy.orm import Session

from classic.components import component

from .transactions import TransactionContext


@component
class BaseRepository:
    """
    Base class for Repositories, using SQLAlchemy
    """
    context: TransactionContext

    @property
    def session(self) -> Session:
        return self.context.current_session
