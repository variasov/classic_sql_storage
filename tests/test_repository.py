
def test_repository(repository):
    repository.write()

    assert repository.read() == [(1, 1)]
