import json

from . import MemoryManager


class JSONMemoryManager(MemoryManager):
    def __init__(self, filename="memory/history.json"):
        self.filename = filename
        try:
            with open(filename) as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = {}

    def store(self, key, role, text):
        self.history[key] = self.history.get(key, [])
        self.history[key].append({"role": role, "text": text})
        with open(self.filename, "w") as f:
            json.dump(self.history, f)

    def retrieve(self, key):
        return self.history.get(key, [])

    def clear(self):
        self.history = {}
        with open(self.filename, "w") as f:
            json.dump(self.history, f)
