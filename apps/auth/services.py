# -*- coding: utf-8 -*-
from .schemas import LoginUser, RegisterUser
from .repository import AuthRepository
from apps.user.services import UserService

class AuthService:
    def __init__(self):
        self.auth_repo = AuthRepository()
        self.user_service = UserService()

    def register_user(self, data: RegisterUser):
        
        return self.user_service.create_user(data)

    def login_user(self, data: LoginUser):
        user = self.auth_repo.authenticate_user(data.username, data.password)
        
        return {"access_token": "fake_token", "refresh_token": "fake_refresh"}