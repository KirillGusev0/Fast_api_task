# -*- coding: utf-8 -*-

from fastapi import  APIRouter
from .services import AuthService
from .schemas import RegisterUser, LoginUser, Token
from apps.user.schemas import UserRead

router = APIRouter()
service = AuthService()

@router.post("/register", response_model=UserRead)
def register_user(data: RegisterUser):
    return service.register_user(data)

@router.post("/login", response_model=Token)
def login_user(data: LoginUser):
    return service.login_user(data)