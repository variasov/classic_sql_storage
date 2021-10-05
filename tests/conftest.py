import pytest

from classic.components import component
from classic.sql_storage import TransactionContext, BaseRepository
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, select


metadata = MetaData()
values = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('value', Integer),
)


@component
class Repository(BaseRepository):

    def write(self):
        self.session.execute(
            values.insert().values(value=1)
        )

    def read(self):
        rows = self.session.execute(
            select(values)
        )
        return [tuple(row) for row in rows]


@pytest.fixture
def engine():
    engine = create_engine('sqlite:///')
    metadata.create_all(engine)
    return engine


@pytest.fixture
def transaction(engine):
    return TransactionContext(bind=engine)


@pytest.fixture
def repository(transaction):
    return Repository(context=transaction)


@pytest.fixture
def service(transaction, repository):

    @component
    class Service:
        repository: Repository

        @transaction
        def write(self):
            self.repository.write()

        @transaction
        def write_many(self):
            self.write()
            self.repository.write()

        @transaction
        def read(self):
            return self.repository.read()

    return Service(repository=repository)
