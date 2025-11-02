# -*- coding: utf-8 -*-
from in_memory_store import InMemoryStore
from .models import User

class UserRepository:
    def __init__(self):
        self.store = InMemoryStore()

    def create(self, user: User):
        return self.store.add(user)

    def get_all(self):
        return self.store.all()

    def get_by_id(self, user_id: int):
        return self.store.get(user_id)

    def update(self, user_id: int, data: dict):
        return self.store.update(user_id, data)

    def delete(self, user_id: int):
        return self.store.delete(user_id)
        