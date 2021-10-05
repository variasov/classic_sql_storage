# Classic SQL Storage

This package provides contextual transactions processing for SQLAlchemy and 
base for pattern "Repository".

Part of project "Classic".

Usage:

```python
from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine, text


engine = create_engine('sqlite:///')

transaction = TransactionContext(bind=engine)


# As context manager:
with transaction:
    transaction.current_session.execute(
        text('SELECT 1')
    )


# As decorator:
@transaction
def some_work():
    transaction.current_session.execute(
        text('SELECT 1')
    )


# Propagation:
@transaction
def complex_function():
    """Doing complex work with db.
    Session will be commited only after finish of complex_function call.
    TransactionContext will count all calls, and will commit or rollback session
    only in last call.
    """
    some_work()
    some_work()
    some_work()
    
    with transaction:
        transaction.current_session.execute(
            text('SELECT 1')
        )


# Automatic rollback
@transaction
def function_with_error():
    """Changes, made by some_work, will be cancelled after raising error"""
    some_work()
    raise ValueError()


```

