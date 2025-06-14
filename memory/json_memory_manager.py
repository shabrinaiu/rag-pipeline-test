import json

from . import MemoryManager


class JSONMemoryManager(MemoryManager):
    """
    JSON-backed implementation of MemoryManager for persistent conversation memory.
    Stores conversation history in a JSON file.
    """

    def __init__(self, filename="memory/history.json"):
        self.filename = filename
        try:
            with open(filename) as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = {}

    def store(self, key, role, text):
        """
        Store a conversation turn (role, text) under a session key.
        """
        self.history[key] = self.history.get(key, [])
        self.history[key].append({"role": role, "text": text})
        with open(self.filename, "w") as f:
            json.dump(self.history, f)

    def retrieve(self, key):
        """
        Retrieve conversation history for a given session key.
        """
        return self.history.get(key, [])

    def clear(self):
        """
        Clear all stored conversation history.
        """
        self.history = {}
        with open(self.filename, "w") as f:
            json.dump(self.history, f)
