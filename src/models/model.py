class MainModel:
    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1
        return self._counter