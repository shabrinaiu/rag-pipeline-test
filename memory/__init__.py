from typing import Any, List


class MemoryManager:
    """
    Abstract base class for conversation memory management.
    Subclasses should implement methods for storing, retrieving, and clearing memory.
    """

    def __init__(self):
        pass

    def store(self, key, role, text):
        """
        Store a conversation turn (role, text) under a session key.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("store method must be implemented by subclasses")

    def retrieve(self, key) -> List[Any]:
        """
        Retrieve conversation history for a given session key.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("retrieve method must be implemented by subclasses")

    def clear(self):
        """
        Clear all stored conversation history.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("clear method must be implemented by subclasses")
