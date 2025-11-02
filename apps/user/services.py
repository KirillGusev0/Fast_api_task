# -*- coding: utf-8 -*-

from .repository import UserRepository
from .schemas import UserCreate
from .models import User
from passlib.hash import bcrypt


def hash_password(password: str) -> str:
    return bcrypt.hash(password)

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, data: UserCreate):
        hashed_pwd = hash_password(data.password)
        new_user = User(
            name=data.name,
            username=data.username,
            password=hashed_pwd,
            email=data.email
        )
        return self.repo.create_user(new_user)

    def get_all(self):
        return self.repo.get_all()
    
    
    def get_by_id(self, num):
        return self.repo.get_by_id(num)
    
    def delete_user(self,num):
        return self.repo.delete_user(num)
    
    def update_user(self, num, new_data):
        return self.repo.update_user(num, **new_data)
    
    
        