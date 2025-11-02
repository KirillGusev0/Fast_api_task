# -*- coding: utf-8 -*-
from fastapi import  APIRouter
from .services import UserService
from .schemas import UserCreate, UserRead

user_router = APIRouter()
service = UserService()

@user_router.get("/", response_model=list[UserRead])
def get_users():
    return service.get_all()

@user_router.post("/", response_model=UserRead)
def create_user(user: UserCreate):
    return service.create_user(user)


@user_router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int):
    return service.get_by_id(user_id)


@user_router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, data: UserCreate):
    return service.update_user(user_id, data.model_dump())

@user_router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int):
    return service.delete_user(user_id)