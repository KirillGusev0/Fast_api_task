# -*- coding: utf-8 -*-

# apps/auth/repository.py
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import bcrypt

from apps.user.repository import UserRepository
from apps.user.models import User
from apps.auth.schemas import RegisterUser, LoginUser


class AuthRepository:
   
    def __init__(self):
        self.user_repo = UserRepository()

    async def register_user(self, db: AsyncSession, payload: RegisterUser) -> User:
        """
        SQL:
        
        SELECT id FROM users WHERE username = :username LIMIT 1;

        
        INSERT INTO users (name, username, hashed_password, email, created_at)
        VALUES (:name, :username, :hashed_password, :email, now())
        RETURNING *;
        """
        # проверка есть ли юзер
        exists = await self.user_repo.get_by_username(db, payload.username)
        if exists:
            raise ValueError("User with this username already exists")

        hashed = bcrypt.hash(payload.password)
        user = User(
            name=payload.name,
            username=payload.username,
            hashed_password=hashed,
            email=payload.email
        )
        return await self.user_repo.create(db, user)

    async def authenticate_user(self, db: AsyncSession, payload: LoginUser) -> Optional[User]:
        """
        SQL:
        SELECT * FROM users WHERE username = :username LIMIT 1;
        
        """
        user = await self.user_repo.get_by_username(db, payload.username)
        if not user:
            return None
        if not bcrypt.verify(payload.password, user.hashed_password):
            return None
        return user

