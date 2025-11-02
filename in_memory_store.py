# -*- coding: utf-8 -*-
class InMemoryStore:
    #Generic in-memory store, acting like a database table
    def __init__(self):
        self._data = []
        self._counter = 1

    def add(self, obj):
        obj.id = self._counter
        self._counter += 1
        self._data.append(obj)
        return obj

    def all(self):
        return self._data

    def get(self, id):
        for item in self._data:
            if item.id == id:
                return item
        raise ValueError("Item not found")

    def update(self, id, data):
        obj = self.get(id)
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj

    def delete(self, id):
        obj = self.get(id)
        self._data.remove(obj)
        return obj