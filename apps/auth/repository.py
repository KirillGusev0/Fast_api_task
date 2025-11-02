# -*- coding: utf-8 -*-

from apps.user.repository import UserRepository
from passlib.hash import bcrypt


class AuthRepository:
    def __init__(self):
        self.user_repo = UserRepository()

    def authenticate_user(self, username: str, password: str):
        
        users = self.user_repo.storage.get_all()
       
            
        for user in users:
            if user.name == username:
                if bcrypt.verify(password, user.password):
                    return user
        raise ValueError("User not found")
        