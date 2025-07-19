class Stack:
    def __init__(self, items=None, limit=100):
        self._container = list(items) if items else []
        self.limit = limit

    @property
    def items(self):
        return self._container

    def isEmpty(self):
        return len(self._container) == 0

    def push(self, item):
        if len(self._container) < self.limit:
            self._container.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self._container.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._container[-1]

    def size(self):
        return len(self._container)

    def full(self):
        return len(self._container) == self.limit

    def search(self, target):
        for idx, item in enumerate(reversed(self._container)):
            if item == target:
                return idx
        return -1
