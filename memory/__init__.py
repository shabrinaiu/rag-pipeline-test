from typing import Any, List


class MemoryManager:
    def __init__(self):
        pass

    def store(self, key, role, text):
        raise NotImplementedError("store method must be implemented by subclasses")

    def retrieve(self, key) -> List[Any]:
        raise NotImplementedError("retrieve method must be implemented by subclasses")

    def clear(self):
        raise NotImplementedError("clear method must be implemented by subclasses")
