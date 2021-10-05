

def test_context_as_context_manager(transaction, repository):
    with transaction:
        repository.write()

    with transaction:
        assert repository.read() == [(1, 1)]


def test_context_as_decorator(service):
    service.write()

    assert service.read() == [(1, 1)]


def test_context_as_decorator_with_propagation(service):
    service.write_many()

    assert service.read() == [(1, 1), (2, 1)]
