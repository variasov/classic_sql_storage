import threading


class Counter:

    def __init__(self):
        self._calls_count = 0

    def increment(self):
        self._calls_count += 1

    def decrement(self):
        self._calls_count -= 1

    @property
    def is_last(self):
        return self._calls_count == 0

    @property
    def is_first(self):
        return self._calls_count == 1


class ThreadSafeCounter(Counter, threading.local):
    pass
